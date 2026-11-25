from abc import ABC, abstractmethod
from datetime import datetime


class Account(ABC):
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance
        self.transactions = []

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return

        self.__balance += amount
        self.transactions.append(
            f"Deposited Rs.{amount:.2f}"
        )
        print("Deposit successful!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return

        if amount > self.__balance:
            print("Insufficient balance!")
            return

        self.__balance -= amount
        self.transactions.append(
            f"Withdrawn Rs.{amount:.2f}"
        )
        print("Withdrawal successful!")

    @abstractmethod
    def account_type(self):
        pass

    def show_history(self):
        print("\nTransaction History:")

        if not self.transactions:
            print("No transactions yet.")
        else:
            for item in self.transactions:
                print(item)


class SavingsAccount(Account):
    def account_type(self):
        return "Savings Account"


class CurrentAccount(Account):
    def account_type(self):
        return "Current Account"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number, account_type):
        if account_number in self.accounts:
            print("Account number already exists!")
            return

        if account_type == "1":
            account = SavingsAccount(name, account_number)
        elif account_type == "2":
            account = CurrentAccount(name, account_number)
        else:
            print("Invalid account type!")
            return

        self.accounts[account_number] = account

        account.transactions.append(
            f"Account created on {datetime.now()}"
        )

        print("Account created successfully!")

    def get_account(self, account_number):
        return self.accounts.get(account_number)
