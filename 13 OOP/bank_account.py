class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def __str__(self):
        return "Account balance: {}".format(self.balance)


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(50)
    print("Balance: {}".format(account.balance))
    account.withdraw(75)
    print("Balance: {}".format(account.balance))
    account.withdraw(500)
    print("Balance: {}".format(account.balance))


if __name__ == "__main__":
    main()
