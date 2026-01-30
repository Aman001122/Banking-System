import json
import os

FILE = "accounts.json"

def load_accounts():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_accounts(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
