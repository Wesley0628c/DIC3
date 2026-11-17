"""Run all five real Streamlit pages against an isolated SQLite database."""
import os
from pathlib import Path
import subprocess
import sys


def test_all_pages_and_cancel(tmp_path):
    # Isolate module globals/config from other service tests.
    code = """
from streamlit.testing.v1 import AppTest
from src.ui.styles import NAV_PAGES
app = AppTest.from_file('src/ui/app.py', default_timeout=30).run()
assert not app.exception, list(app.exception)
for page in NAV_PAGES:
    app.sidebar.radio[0].set_value(page).run()
    assert not app.exception, (page, list(app.exception))
app.sidebar.radio[0].set_value(NAV_PAGES[0]).run()
next(b for b in app.button if b.label == '＋ 新增食材').click().run()
assert not app.exception, list(app.exception)
next(b for b in app.button if b.label == '取消').click().run()
assert not app.exception, list(app.exception)
from src.database.db_manager import DatabaseManager
with DatabaseManager().connection() as conn:
    assert conn.execute('SELECT COUNT(*) FROM inventory_items').fetchone()[0] == 0
from scripts.seed_demo import seed
from src.config import DATABASE_PATH
seed(DATABASE_PATH)
for page in NAV_PAGES:
    app.sidebar.radio[0].set_value(page).run()
    assert not app.exception, (page, list(app.exception))
app.sidebar.radio[0].set_value(NAV_PAGES[1]).run()
next(b for b in app.button if b.label == '已使用').click().run()
assert not app.exception, list(app.exception)
next(n for n in app.number_input if n.label == '本次使用').set_value(1.0).run()
next(b for b in app.button if b.label == '取消').click().run()
with DatabaseManager().connection() as conn:
    assert conn.execute('SELECT quantity FROM inventory_items WHERE id=1').fetchone()[0] == 2
next(b for b in app.button if b.label == '已使用').click().run()
next(n for n in app.number_input if n.label == '本次使用').set_value(1.0).run()
next(b for b in app.button if b.label == '確認使用').click().run()
assert not app.exception, list(app.exception)
with DatabaseManager().connection() as conn:
    assert conn.execute('SELECT quantity FROM inventory_items WHERE id=1').fetchone()[0] == 1
    assert conn.execute('SELECT COUNT(*) FROM consumption_waste_logs').fetchone()[0] == 1
app.sidebar.radio[0].set_value(NAV_PAGES[4]).run()
assert not app.exception, list(app.exception)
"""
    env = dict(os.environ, DATABASE_PATH=str(tmp_path / "ui.db"), OPENAI_API_KEY="",
               GOOGLE_API_KEY="", GEMINI_API_KEY="", RAG_ENABLED="false")
    result = subprocess.run([sys.executable, "-c", code], cwd=Path(__file__).resolve().parents[1],
                            env=env, capture_output=True, text=True, timeout=120)
    assert result.returncode == 0, result.stdout + result.stderr
