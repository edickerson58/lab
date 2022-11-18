class Account:
    def __init__(self, name: str):
        """
        Constructor function to initialize the name and balance associated with an account
        :param name: Name of the user
        """
        self.account_name: str = name
        self.account_balance: float = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to add an amount to the account balance
        :param amount: The number that will increase the account balance
        :return: Returns a boolean value based on if the transaction was successful or not
        """
        increment: float = amount

        if increment < 0 or increment == 0:
            return False
        else:
            self.account_balance += increment
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Method to withdraw an amount from the account balance
        :param amount: The number that will decrease the account balance
        :return: Returns a boolean value based on if the transaction was successful or not
        """
        decrement: float = amount

        if decrement < 0 or decrement == 0 or decrement > self.account_balance:
            return False
        else:
            self.account_balance -= decrement
            return True

    def get_balance(self) -> float:
        return self.account_balance

    def get_name(self) -> str:
        return self.account_name
