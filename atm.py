from database import load_accounts, save_accounts
from utils import line, get_amount
from datetime import datetime

def atm_menu(acc):
    while True:
        data = load_accounts()
        line()
        print(f"Welcome, {data[acc]['name']}")
        print("1 Deposit")
        print("2 Withdraw")
        print("3 Transfer")
        print("4 Balance")
        print("5 Mini Statement")
        print("6 Logout")
        line()

        ch = input("Choose option: ")

        if ch == "1":
            amt = get_amount()
            if amt:
                data[acc]["balance"] += amt
                data[acc]["transactions"].append(f"{datetime.now()} +{amt}")
                save_accounts(data)
                print("Deposit successful")

        elif ch == "2":
            amt = get_amount()
            if amt and amt <= data[acc]["balance"]:
                data[acc]["balance"] -= amt
                data[acc]["transactions"].append(f"{datetime.now()} -{amt}")
                save_accounts(data)
                print("Withdrawal successful")
            else:
                print("Insufficient balance")

        elif ch == "3":
            to = input("Receiver account number: ")
            amt = get_amount()
            if to in data and amt and amt <= data[acc]["balance"]:
                data[acc]["balance"] -= amt
                data[to]["balance"] += amt
                data[acc]["transactions"].append(f"{datetime.now()} Sent {amt} to {to}")
                data[to]["transactions"].append(f"{datetime.now()} Received {amt} from {acc}")
                save_accounts(data)
                print("Transfer successful")
            else:
                print("Transfer failed")

        elif ch == "4":
            print("Current Balance:", data[acc]["balance"])

        elif ch == "5":
            print("Last Transactions:")
            for t in data[acc]["transactions"][-5:]:
                print(t)

        elif ch == "6":
            break
