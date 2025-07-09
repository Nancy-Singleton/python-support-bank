import csv
import json
from datetime import datetime
from transaction import Transaction

def process_transaction_file(bank, file_path):
    if file_path.endswith(".csv"):
        process_csv_transaction_file(bank, file_path)
    elif file_path.endswith(".json"):
        process_json_transaction_file(bank, file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a .csv or .json file.")


def process_csv_transaction_file(bank, file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    transactions = []
    for row in data:
        transaction = Transaction(
            datetime.strptime(row['Date'], "%d/%m/%Y"),
            row['From'],
            row['To'],
            row['Narrative'],
            parse_transaction_amount(row['Amount'])
        )
        transactions.append(transaction)

    process_transactions(bank, transactions)


def process_json_transaction_file(bank, file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    transactions = []
    for row in data:
        transaction = Transaction(
            datetime.strptime(row['Date'], "%Y-%m-%dT%H:%M:%S"),
            row['FromAccount'],
            row['ToAccount'],
            row['Narrative'],
            parse_transaction_amount(row['Amount'])
        )
        transactions.append(transaction)

    process_transactions(bank, transactions)


def process_transactions(bank, transactions):
    for transaction in transactions:
        bank.process_transaction(transaction)


def parse_transaction_amount(amount):
    return float(amount) * 100