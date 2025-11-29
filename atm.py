from database import load_db, save_db
from utils import log_transaction

def auth():
    db = load_db()
    acc = input("Enter Account Number: ").strip()
    if acc not in db:
        print("Account not found")
        return None
    for _ in range(3):
        pin = input("Enter PIN: ").strip()
        if pin == db[acc]["pin"]:
            return acc
        print("Wrong PIN")
    print("Account locked after 3 wrong attempts")
    return None

def balance(acc):
    db = load_db()
    print("Balance:", db[acc]["balance"])

def deposit(acc):
    db = load_db()
    amt = input("Amount: ").strip()
    if not amt.isdigit():
        print("Invalid")
        return
    amt = int(amt)
    db[acc]["balance"] += amt
    log_transaction(db[acc], f"Deposit +{amt}")
    save_db(db)
    print("Deposited")

def withdraw(acc):
    db = load_db()
    amt = input("Amount: ").strip()
    if not amt.isdigit():
        print("Invalid")
        return
    amt = int(amt)
    if amt > db[acc]["balance"]:
        print("Insufficient funds")
        return
    db[acc]["balance"] -= amt
    log_transaction(db[acc], f"Withdraw -{amt}")
    save_db(db)
    print("Withdrawn")

def transfer(acc):
    db = load_db()
    target = input("Target Account: ").strip()
    if target not in db:
        print("Target account not found")
        return
    amt = input("Amount: ").strip()
    if not amt.isdigit():
        print("Invalid")
        return
    amt = int(amt)
    if amt > db[acc]["balance"]:
        print("Insufficient funds")
        return
    db[acc]["balance"] -= amt
    db[target]["balance"] += amt
    log_transaction(db[acc], f"Transfer to {target} -{amt}")
    log_transaction(db[target], f"Transfer from {acc} +{amt}")
    save_db(db)
    print("Transferred")

def mini_statement(acc):
    db = load_db()
    for t in db[acc]["transactions"]:
        print(t)
