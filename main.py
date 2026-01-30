from database import load_accounts, save_accounts
from atm import atm_menu
from utils import line, get_pin

def create_account():
    data = load_accounts()
    acc = input("Choose account number: ")

    if acc in data:
        print("Account already exists")
        return

    name = input("Enter name: ")
    pin = get_pin()
    if not pin:
        print("Invalid PIN")
        return

    data[acc] = {
        "name": name,
        "pin": pin,
        "balance": 0,
        "transactions": []
    }

    save_accounts(data)
    print("Account created successfully")

def delete_account():
    data = load_accounts()
    acc = input("Enter account number: ")

    if acc not in data:
        print("Account not found")
        return

    pin = input("Enter PIN to confirm deletion: ")

    if data[acc]["pin"] != pin:
        print("Incorrect PIN")
        return

    confirm = input("Type YES to confirm deletion: ")
    if confirm == "YES":
        del data[acc]
        save_accounts(data)
        print("Account deleted successfully")
    else:
        print("Deletion cancelled")

def login():
    data = load_accounts()
    attempts = 3

    while attempts > 0:
        acc = input("Account number: ")
        pin = input("PIN: ")

        if acc in data and data[acc]["pin"] == pin:
            return acc

        attempts -= 1
        print("Invalid credentials")

    print("Account locked")
    return None

while True:
    line()
    print("BANKING & ATM SYSTEM")
    print("1 Login")
    print("2 Create Account")
    print("3 Delete Account")
    print("4 Exit")
    line()

    ch = input("Choose option: ")

    if ch == "1":
        acc = login()
        if acc:
            atm_menu(acc)

    elif ch == "2":
        create_account()

    elif ch == "3":
        delete_account()

    elif ch == "4":
        break
