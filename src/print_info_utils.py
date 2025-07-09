def list_all(bank):
    for account in bank.accounts:
        print(f"{account.name}: {format_amount(account.balance)}")


def list_account(bank, account_name):
    account = bank.get_existing_account(account_name)
    if not account:
        print(f"Account {account_name} does not exist.")
        return

    for transaction in account.transactions:
        print(
            f"Date: {transaction.date.strftime('%d/%m/%Y')}, From: {transaction.from_}, To: {transaction.to}, Narrative: {transaction.narrative}, Amount: {format_amount(transaction.amount)}")


def format_amount(amount):
    is_negative = amount < 0
    absolute_amount = abs(amount)
    return f"{'−' if is_negative else ''}£{absolute_amount / 100:.2f}"