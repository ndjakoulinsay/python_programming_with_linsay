
DEFAULT_BANK_ACCOUNT_NUMBER = "123"
accounts = []

class Account:
    def __init__(self, acc_number, holder, balance=0, account_limit=0, overdraft_limit=0):
        self.acc_number = acc_number
        self.holder = holder
        self.balance = balance
        self.account_limit = account_limit
        self.overdraft_limit = overdraft_limit
        
    def __str__(self):
        return f"Holder: {self.holder} | Account Number: {self.acc_number} | Balance: {self.balance} | Account Limit: {self.account_limit} | Overdraft Limit: {self.overdraft_limit}"

def list_accounts():
    print("\n--- List of Accounts ---")
    for account in accounts:
        print(account)
        
def create_account():
    account_number=input("Enter account number: ")
    holder_name=input("Enter account holder name: ")
    account_limit=input("Enter account limit: ") 
    overdraft_limit=input("Enter overdraft limit: ")
    new_account = Account(account_number, holder_name, 0, account_limit, overdraft_limit)
    accounts.append(new_account) 
    
    
def deposit():
    account_number=input("Enter account number: ")
    amount=input("Enter amount to deposit: ")
    for account in accounts:
        if account.acc_number == account_number:
            account.balance += amount
            print(f"Deposited {amount} to account {account_number}. New balance: {account.balance}") 
            
def withdraw():
    account_number=input("Enter account number: ")
    amount=input("Enter amount to withdraw: ")
    for account in accounts:
        if account.acc_number == account_number:
            if account.balance + account.overdraft_limit >= amount:
                account.balance -= amount
                print(f"Withdrew {amount} from account {account_number}. New balance: {account.balance}")
            else:
               print(f"Insufficient funds for withdrawal from account {account_number}. Available balance and overdraft limit: {account.balance + account.overdraft_limit}")                            

def check_balance():
    account_number=input("Enter account number: ")
    for account in accounts:
        if account.acc_number == account_number:
            print(f"Account {account_number} balance: {account.balance}")
            return
    print(f"Account {account_number} not found.")
    
def transfer():
    from_account_number=input("Enter source account number: ")
    to_account_number=input("Enter destination account number: ")
    amount=input("Enter amount to transfer: ")
    
    from_account = None
    to_account = None
    
    for account in accounts:
        if account.acc_number == from_account_number:
            from_account = account
        if account.acc_number == to_account_number:
            to_account = account
            
    if from_account is None:
        print(f"Source account {from_account_number} not found.")
        return
    if to_account is None:
        print(f"Destination account {to_account_number} not found.")
        return
    
    if from_account.balance + from_account.overdraft_limit >= amount:
        from_account.balance -= amount
        to_account.balance += amount
        print(f"Transferred {amount} from account {from_account_number} to account {to_account_number}. New balance of source account: {from_account.balance}, New balance of destination account: {to_account.balance}")
    else:
        print(f"Insufficient funds for transfer from account {from_account_number}. Available balance and overdraft limit: {from_account.balance + from_account.overdraft_limit}")
        
def list_all_transactions():
    print("\n--- List of All Transactions ---")
    # This function would list all transactions. For now, it's a placeholder.
 
def list_transactions_for_account():
    account_number=input("Enter account number: ")
    print(f"\n--- List of Transactions for Account {account_number} ---")
    # This function would list transactions for a specific account. For now, it's a placeholder.  
                   
def display_menu():
    print("\n--- Bank Application Menu ---")
    print("1. Create Account")  
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. transfer")
    print("6. list accounts")
    print("7. list all transactions")
    print("8. list transactions for an account")
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
            transfer
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