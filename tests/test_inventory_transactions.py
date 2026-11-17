"""Regression checks for actual persistence, rollback, racing writes and reminders."""
from concurrent.futures import ThreadPoolExecutor
from datetime import date
import sqlite3
import pytest

from src.database.db_manager import DatabaseManager
from src.services.inventory_service import InventoryService
from src.services.analytics_service import AnalyticsService
from src.services.reminder_service import ReminderService
from src.services.portion_service import classify_item, recommend_for_servings
from scripts.seed_demo import seed


@pytest.fixture
def service(tmp_path):
    db = DatabaseManager(str(tmp_path / "inventory.db"))
    db.initialize_database()
    return InventoryService(db)


def add(service, **updates):
    data = dict(name="雞蛋", category="egg_dairy", quantity=10, unit="piece",
                purchase_date="2026-11-17", expiry_date="2026-11-20",
                date_label_type="use_by", opened_date=None, storage_location="refrigerator")
    data.update(updates)
    return service.add_item(data)


def log_count(service):
    with service.db.connection() as conn:
        return conn.execute("SELECT COUNT(*) FROM consumption_waste_logs").fetchone()[0]


@pytest.mark.parametrize("value", [float("nan"), float("inf"), True, -1, 0])
def test_invalid_quantities_do_not_insert(service, value):
    with pytest.raises(ValueError):
        add(service, quantity=value)
    assert service.get_items() == []


def test_cancel_and_idempotency(service):
    item = add(service)
    # Cancelling does not call the mutation service.
    assert service.get_item_by_id(item)["quantity"] == 10
    assert log_count(service) == 0
    service.consume_item(item, 3, operation_id="confirm-1", expected_quantity=10)
    service.consume_item(item, 3, operation_id="confirm-1", expected_quantity=10)
    assert service.get_item_by_id(item)["quantity"] == 7
    assert log_count(service) == 1
    with pytest.raises(ValueError):
        service.consume_item(item, 2, operation_id="confirm-1")
    with pytest.raises(ValueError):
        service.consume_item(item, 1, operation_id="stale", expected_quantity=10)
    assert service.get_item_by_id(item)["quantity"] == 7


def test_rollback_if_log_fails(service):
    item = add(service)
    with service.db.connection() as conn:
        conn.execute("CREATE TRIGGER reject_event BEFORE INSERT ON consumption_waste_logs BEGIN SELECT RAISE(ABORT, 'injected failure'); END")
    with pytest.raises(sqlite3.IntegrityError):
        service.consume_item(item, 3, operation_id="failed")
    assert service.get_item_by_id(item)["quantity"] == 10
    assert log_count(service) == 0
    with service.db.connection() as conn:
        assert conn.execute("SELECT COUNT(*) FROM operation_receipts").fetchone()[0] == 0


def test_concurrent_consumption(service):
    item = add(service)
    def consume(index):
        try:
            service.consume_item(item, 7, operation_id=f"concurrent-{index}")
            return True
        except ValueError:
            return False
    with ThreadPoolExecutor(max_workers=2) as pool:
        assert sorted(pool.map(consume, [1, 2])) == [False, True]
    assert service.get_item_by_id(item)["quantity"] == 3
    assert log_count(service) == 1


def test_history_survives_deleted_input(service):
    item = add(service)
    service.waste_item(item, 2, reason="spoiled")
    service.delete_item(item)
    with service.db.connection() as conn:
        log = dict(conn.execute("SELECT * FROM consumption_waste_logs").fetchone())
    assert log["item_id"] is None and log["item_name"] == "雞蛋"


def test_reminder_boundaries(service):
    reminder = ReminderService(3, service, today=date(2026, 11, 17))
    for value, status in [(None, "no_date"), ("2026-11-16", "passed_date"),
                          ("2026-11-17", "expiring_soon"), ("2026-11-20", "expiring_soon"),
                          ("2026-11-21", "normal")]:
        assert reminder.get_reminder_status(value) == status


def test_analytics_keeps_units_and_denominator(service):
    eggs = add(service)
    flour = add(service, name="麵粉", quantity=500, unit="g", category="staple")
    service.consume_item(eggs, 3)
    service.waste_item(eggs, 1)
    service.consume_item(flour, 100)
    data = AnalyticsService(service.db).get_waste_reduction_kpis()
    assert data["by_unit"]["piece"]["waste_rate"] == 25
    assert data["by_unit"]["g"]["consumed"] == 100
    assert data["total_events"] == 3


def test_missing_date_requires_review_and_exclusion_filters(service):
    item = add(service, expiry_date=None, date_label_type=None)
    assert classify_item(service.get_item_by_id(item))[0] == "review"
    results = recommend_for_servings(service.get_items(), excluded_ingredients=["雞蛋"])
    assert not results


def test_seed_is_repeat_safe(tmp_path):
    path = tmp_path / "seed.db"
    count = seed(path, date(2026, 11, 17))
    assert count == 25
    with pytest.raises(ValueError):
        seed(path)
    assert len(InventoryService(DatabaseManager(str(path))).get_items()) == 25
