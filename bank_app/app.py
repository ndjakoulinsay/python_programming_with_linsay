
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

def display_menu():
    pass

if __name__ == "__main__":
    default_account = Account(DEFAULT_BANK_ACCOUNT_NUMBER, "Bank", 1000000)
    accounts.append(default_account)
    print(accounts[0])
    
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "9":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")