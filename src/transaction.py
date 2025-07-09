class Transaction:
    def __init__(self, date, from_, to, narrative, amount):
        self.date = date
        self.from_ = from_  # 'from' is a Python keyword, so we use 'from_'
        self.to = to
        self.narrative = narrative
        self.amount = amount