from datetime import datetime

def log_transaction(account, message):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    account["transactions"].append(f"{ts} - {message}")
    if len(account["transactions"]) > 10:
        account["transactions"] = account["transactions"][-10:]
