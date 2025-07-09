class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []

    def debit(self, transaction):
        self.balance -= transaction.amount
        self.transactions.append(transaction)

    def credit(self, transaction):
        self.balance += transaction.amount
        self.transactions.append(transaction)