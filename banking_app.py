class Account:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be greater than 0."
        self.balance += amount
        self.transactions.append(f"Deposited {amount:.2f}")
        return True, f"Deposited {amount:.2f} successfully."

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be greater than 0."
        if amount > self.balance:
            return False, "Insufficient balance."
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount:.2f}")
        return True, f"Withdrew {amount:.2f} successfully."

    def add_transaction(self, message):
        self.transactions.append(message)


class BankingApp:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001

    def create_account(self, owner_name):
        if not owner_name.strip():
            return None, "Owner name cannot be empty."
        account_number = str(self.next_account_number)
        self.next_account_number += 1
        self.accounts[account_number] = Account(owner_name.strip())
        return account_number, f"Account created successfully. Account Number: {account_number}"

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if from_account is None:
            return False, "Source account not found."
        if to_account is None:
            return False, "Destination account not found."
        if from_account_number == to_account_number:
            return False, "Cannot transfer to the same account."
        if amount <= 0:
            return False, "Transfer amount must be greater than 0."
        if amount > from_account.balance:
            return False, "Insufficient balance in source account."

        from_account.balance -= amount
        to_account.balance += amount
        from_account.add_transaction(f"Transferred {amount:.2f} to account {to_account_number}")
        to_account.add_transaction(f"Received {amount:.2f} from account {from_account_number}")
        return True, f"Transferred {amount:.2f} successfully."

    def list_accounts(self):
        if not self.accounts:
            print("No accounts created yet.")
            return
        print("\nAccounts:")
        for number, account in self.accounts.items():
            print(f"- {number}: {account.owner_name} | Balance: {account.balance:.2f}")


def show_menu():
    print("\n=== Banking App CLI ===")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check Balance")
    print("6. Show Transaction History")
    print("7. List Accounts")
    print("0. Exit")


def read_amount(prompt):
    raw_value = input(prompt).strip()
    amount = float(raw_value)
    return amount


def main():
    app = BankingApp()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            owner_name = input("Enter account owner name: ")
            account_number, message = app.create_account(owner_name)
            print(message)
            if account_number:
                print(f"Please save account number: {account_number}")

        elif choice == "2":
            account_number = input("Enter account number: ").strip()
            account = app.get_account(account_number)
            if account is None:
                print("Account not found.")
                continue
            amount = read_amount("Enter deposit amount: ")
            success, message = account.deposit(amount)
            print(message)

        elif choice == "3":
            account_number = input("Enter account number: ").strip()
            account = app.get_account(account_number)
            if account is None:
                print("Account not found.")
                continue
            amount = read_amount("Enter withdrawal amount: ")
            success, message = account.withdraw(amount)
            print(message)

        elif choice == "4":
            from_account_number = input("Enter source account number: ").strip()
            to_account_number = input("Enter destination account number: ").strip()
            amount = read_amount("Enter transfer amount: ")
            success, message = app.transfer(from_account_number, to_account_number, amount)
            print(message)

        elif choice == "5":
            account_number = input("Enter account number: ").strip()
            account = app.get_account(account_number)
            if account is None:
                print("Account not found.")
                continue
            print(f"Current balance: {account.balance:.2f}")

        elif choice == "6":
            account_number = input("Enter account number: ").strip()
            account = app.get_account(account_number)
            if account is None:
                print("Account not found.")
                continue
            if not account.transactions:
                print("No transactions yet.")
            else:
                print("\nTransaction history:")
                for txn in account.transactions:
                    print(f"- {txn}")

        elif choice == "7":
            app.list_accounts()

        elif choice == "0":
            print("Thank you for using Banking App CLI. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
