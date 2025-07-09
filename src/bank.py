from account import Account
import math

class Bank:
    def __init__(self):
        self.accounts = []

    def get_existing_account(self, name):
        for account in self.accounts:
            if account.name == name:
                return account
        return None

    def get_account(self, name):
        existing_account = self.get_existing_account(name)
        if existing_account:
            return existing_account

        new_account = Account(name)
        self.accounts.append(new_account)
        return new_account

    def process_transaction(self, transaction):
        if math.isnan(transaction.amount):
            return

        from_account = self.get_account(transaction.from_)
        to_account = self.get_account(transaction.to)

        from_account.debit(transaction)
        to_account.credit(transaction)