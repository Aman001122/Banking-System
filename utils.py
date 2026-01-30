def line():
    print("=" * 40)

def get_amount():
    amt = input("Enter amount: ")
    if amt.isdigit() and int(amt) > 0:
        return int(amt)
    return None

def get_pin():
    pin = input("Set 4-digit PIN: ")
    if pin.isdigit() and len(pin) == 4:
        return pin
    return None
