"""Load synthetic inventory into an EMPTY database; never reset existing records."""
import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.database.db_manager import DatabaseManager
from src.services.inventory_service import InventoryService


def seed(target, reference_date=None):
    today = reference_date or date.today()
    db = DatabaseManager(str(target))
    db.initialize_database()
    service = InventoryService(db)
    with db.connection() as conn:
        conn.execute("BEGIN IMMEDIATE")
        if conn.execute("SELECT COUNT(*) FROM inventory_items").fetchone()[0] or conn.execute("SELECT COUNT(*) FROM consumption_waste_logs").fetchone()[0]:
            raise ValueError("目標資料庫已有資料，請指定另一個 demo 路徑；不會重設資料。")
        # Keep the complete seed atomic, using the same field validation as the service.
        for item in json.loads((ROOT / "data/demo_inventory.json").read_text(encoding="utf-8"))["items"]:
            fields = {key: value for key, value in item.items() if key not in ("expiry_days",)}
            fields.update(purchase_date=today.isoformat(), opened_date=None,
                          expiry_date=(today+timedelta(days=item["expiry_days"])).isoformat() if item["expiry_days"] is not None else None)
            fields["date_label_type"] = fields["date_label_type"] if fields["expiry_date"] else None
            data = service._validate(fields)
            columns = service.FIELDS
            conn.execute("INSERT INTO inventory_items (" + ",".join(columns) + ") VALUES (" + ",".join("?" for _ in columns) + ")", tuple(data[key] for key in columns))
    return len(service.get_items())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", default="data/database/demo.db")
    parser.add_argument("--date", type=date.fromisoformat, default=None, help="固定示範日期；省略則依執行當日")
    args = parser.parse_args()
    try:
        count = seed(ROOT / args.database, args.date)
    except ValueError as exc:
        parser.exit(1, str(exc) + "\n")
    print(f"Loaded {count} synthetic batches into {args.database}. These are not verified food labels.")
