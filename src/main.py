from read_file_utils import process_transaction_file
from bank import Bank
from print_info_utils import list_account, list_all


def main():
    bank = Bank()
    process_transaction_file(bank, "inputs/Transactions2013.json")

    while True:
        user_command = input("Enter a command (List All or List <name>): ")
        if user_command.lower() == "list all":
            list_all(bank)
        elif user_command.lower().startswith("list "):
            list_account(bank, user_command[5:])


if __name__ == "__main__":
    main()