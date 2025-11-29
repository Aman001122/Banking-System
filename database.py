import json
from pathlib import Path

DB_PATH = Path("accounts.json")

def load_db():
    if not DB_PATH.exists():
        DB_PATH.write_text(json.dumps({}, indent=2))
    return json.loads(DB_PATH.read_text())

def save_db(data):
    DB_PATH.write_text(json.dumps(data, indent=2))
