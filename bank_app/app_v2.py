DEFAULT_BANK_ACCOUNT_NUMBER = "123"
accounts = []
transactions = []


class Account:
    def __init__(
        self, acc_number, holder, balance=0, account_limit=0, overdraft_limit=0
    ):
        self.acc_number = acc_number
        self.holder = holder
        self.balance = balance
        self.account_limit = account_limit
        self.overdraft_limit = overdraft_limit
        
    def debit(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True, False  # Indicate that overdraft was not used
        elif self.overdraft_limit > 0 and (self.balance + self.overdraft_limit) >= amount:
            self.balance -= amount
            return True, True  # Indicate that overdraft was used
        else:
            return False, False  # Indicate that debit failed and overdraft was not used
        
    def credit(self, amount):
        if self.balance + amount > self.account_limit:
            return False
        else:
            self.balance += amount
            return True
        
    def print_balance(self):
        print(f"Account {self.acc_number} - {self.holder} balance: {self.balance}")

    def __str__(self):
        return f"Holder: {self.holder} | Account Number: {self.acc_number} | Balance: {self.balance} | Account Limit: {self.account_limit} | Overdraft Limit: {self.overdraft_limit}"


class Transaction:
    def __init__(self, from_account, to_account, amount):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        # TODO: add transaction type (deposit, withdrawal, transfer) and timestamp

    def __str__(self):
        return (
            f"From: {self.from_account} | To: {self.to_account} | Amount: {self.amount}"
        )


def record_transaction(from_account, to_account, amount):
    transaction = Transaction(from_account, to_account, amount)
    transactions.append(transaction)


def find_account(account_number):
    for account in accounts:
        if account.acc_number == account_number:
            return account
    return None


def list_accounts():
    print("\n--- List of Accounts ---")
    for account in accounts:
        print(account)


def create_account():
    account_number = input("Enter account number: ")

    if find_account(account_number) is not None:
        print(f"Account {account_number} already exists.")
        return

    holder_name = input("Enter account holder name: ")
    account_limit = int(input("Enter account limit: "))
    overdraft_limit = int(input("Enter overdraft limit: "))
    new_account = Account(
        account_number, holder_name, 0, account_limit, overdraft_limit
    )
    accounts.append(new_account)

    print(f"Account created successfully: {new_account}")


def deposit():
    account_number = input("Enter account number: ")
    amount = int(input("Enter amount to deposit: "))
    cus_account = find_account(account_number)
    default_account = find_account(DEFAULT_BANK_ACCOUNT_NUMBER)
    if cus_account is None:
        print(f"Account {account_number} not found.")
        return
    elif default_account.debit(amount) is False:
        print(
            f"Insufficient funds in the default bank account for this deposit. Available balance: {default_account.balance}"
        )
        return
    elif cus_account.credit(amount) is False:
        print(
            f"Deposit amount exceeds the account limit for account {account_number}. Available balance: {cus_account.balance}, Account limit: {cus_account.account_limit}"
        )
        default_account.credit(amount)  # Revert the debit from the default account since the credit to the customer's account failed
        return

    record_transaction(
        DEFAULT_BANK_ACCOUNT_NUMBER, account_number, amount
    )  # Record the deposit transaction
    print(
        f"Deposited {amount} to account {account_number}. New balance: {cus_account.balance}"
    )


def withdraw():
    account_number = input("Enter account number: ")
    amount = int(input("Enter amount to withdraw: "))
    cus_account = find_account(account_number)
    default_account = find_account(DEFAULT_BANK_ACCOUNT_NUMBER)
    
    if cus_account is None:
        print(f"Account {account_number} not found.")
        return
    
    success, overdraft_used = cus_account.debit(amount)
    
    if not success:
        if cus_account.overdraft_limit == 0:
            print(
                f"Insufficient funds for withdrawal from account {account_number}. Available balance: {cus_account.balance}"
            )
            return
        else:
            print(
                f"Insufficient funds for withdrawal from account {account_number}. Available balance and overdraft limit: {cus_account.balance + cus_account.overdraft_limit}"
            )
            return

    default_account.credit(amount)  # Add the withdrawn amount back to the default bank account
    record_transaction(
        account_number, DEFAULT_BANK_ACCOUNT_NUMBER, amount
    )  # Record the withdrawal transaction
    print(
        f"Withdrew {amount} from account {account_number}. New balance: {cus_account.balance}"
    )
    if overdraft_used:
        print(
            f"Note: Overdraft used for this withdrawal. Available balance: {cus_account.balance}, Overdraft limit: {cus_account.overdraft_limit}"
        )


def check_balance():
    account_number = input("Enter account number: ")
    account = find_account(account_number)
    if account is None:
        print(f"Account {account_number} not found.")
    else:
        account.print_balance()


def transfer():
    from_account_number = input("Enter source account number: ")
    to_account_number = input("Enter destination account number: ")
    amount = int(input("Enter amount to transfer: "))

    from_account = find_account(from_account_number)
    to_account = find_account(to_account_number)

    if from_account is None:
        print(f"Source account {from_account_number} not found.")
        return
    elif to_account is None:
        print(f"Destination account {to_account_number} not found.")
        return
    elif from_account_number == to_account_number:
        print("Source and destination accounts cannot be the same.")
        return
    elif from_account_number == DEFAULT_BANK_ACCOUNT_NUMBER:
        print(
            f"Cannot transfer from the default bank account. Please use the deposit function to add funds to customer accounts."
        )
        return
    elif to_account_number == DEFAULT_BANK_ACCOUNT_NUMBER:
        print(
            f"Cannot transfer to the default bank account. Please use the withdraw function to remove funds from customer accounts."
        )
        return
    
    from_success, from_overdraft_used = from_account.debit(amount)
    if not from_success:
        if from_account.overdraft_limit == 0:
            print(
                f"Insufficient funds for transfer from account {from_account_number}. Available balance: {from_account.balance}"
            )
            return
        else:
            print(
                f"Insufficient funds for transfer from account {from_account_number}. Available balance and overdraft limit: {from_account.balance + from_account.overdraft_limit}"
            )
            return

    if to_account.credit(amount) is False:
        print(
            f"Transfer amount exceeds the account limit for destination account {to_account_number}. Available balance: {to_account.balance}, Account limit: {to_account.account_limit}"
        )
        from_account.credit(amount)  # Revert the debit from the source account since the credit to the destination account failed
        return

    record_transaction(
        from_account_number, to_account_number, amount
    )  # Record the transfer transaction
    print(
        f"Transferred {amount} from account {from_account_number} to account {to_account_number}. New balance of source account: {from_account.balance}, New balance of destination account: {to_account.balance}"
    )
    
    if from_overdraft_used:
        print(
            f"Note: Overdraft used for this transfer. Available balance of source account: {from_account.balance}, Overdraft limit: {from_account.overdraft_limit}"
        )


def list_all_transactions():
    print("\n--- List of All Transactions ---")
    for transaction in transactions:
        print(transaction)


def list_transactions_for_account():
    account_number = input("Enter account number: ")
    print(f"\n--- List of Transactions for Account {account_number} ---")
    for transaction in transactions:
        if (
            transaction.from_account == account_number
            or transaction.to_account == account_number
        ):
            print(transaction)


def display_menu():
    print("\n--- Bank Application Menu ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transfer")
    print("6. List Accounts")
    print("7. List All Transactions")
    print("8. List Transactions for an Account")
    print("9. Exit")


if __name__ == "__main__":
    default_account = Account(DEFAULT_BANK_ACCOUNT_NUMBER, "Bank", 1000000)
    accounts.append(default_account)
    print(accounts[0])

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transfer()
        elif choice == "6":
            list_accounts()
        elif choice == "7":
            list_all_transactions()
        elif choice == "8":
            list_transactions_for_account()
        elif choice == "9":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
