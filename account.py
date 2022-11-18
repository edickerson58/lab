class Account:
    def __init__(self, name):
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount):
        increment = amount

        if increment < 0 or increment == 0:
            return False
        else:
            self.account_balance += increment
            return True

    def withdraw(self, amount):
        decrement = amount

        if decrement < 0 or decrement == 0 or decrement > self.account_balance:
            return False
        else:
            self.account_balance -= decrement

    def get_balance(self):
        return self.account_balance

    def get_name(self):
        return self.account_name
