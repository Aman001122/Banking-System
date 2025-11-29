from atm import auth, balance, deposit, withdraw, transfer, mini_statement

def menu(acc):
    while True:
        print("""
1 Balance
2 Deposit
3 Withdraw
4 Transfer
5 Mini Statement
0 Exit
""")
        c = input("Choose: ").strip()
        if c == "1":
            balance(acc)
        elif c == "2":
            deposit(acc)
        elif c == "3":
            withdraw(acc)
        elif c == "4":
            transfer(acc)
        elif c == "5":
            mini_statement(acc)
        elif c == "0":
            print("Goodbye")
            break
        else:
            print("Invalid")

def main():
    acc = auth()
    if acc:
        menu(acc)

if __name__ == "__main__":
    main()
