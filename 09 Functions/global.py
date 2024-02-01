balance = 0


def main():
    deposit(100)
    withdraw(50)
    print(balance)


def deposit(amount):
    global balance
    balance += amount


def withdraw(amount):
    global balance
    balance -= amount


print(balance)

if __name__ == "__main__":
    main()
