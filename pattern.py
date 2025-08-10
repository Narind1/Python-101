class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_balance):
        if account_number not in self.accounts:
            self.accounts[account_number] = {"name": name, "balance": initial_balance}
            print("Account created successfully!")
        else:
            print("Account already exists with the given account number.")

    def display_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Balance for account {account_number}: ${self.accounts[account_number]['balance']}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(f"Deposit successful. New balance: ${self.accounts[account_number]['balance']}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                print(f"Withdrawal successful. New balance: ${self.accounts[account_number]['balance']}")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

    def list_accounts(self):
        print("List of Accounts:")
        for account_number, details in self.accounts.items():
            print(f"Account {account_number}: {details['name']} - Balance: ${details['balance']}")

# Example Usage
bank = Bank()

# Creating accounts
bank.create_account(1001, "John Doe", 1000)
bank.create_account(1002, "Jane Doe", 1500)

# Displaying account balances
bank.display_balance(1001)
bank.display_balance(1002)

# Making transactions
bank.deposit(1001, 500)
bank.withdraw(1002, 200)

# Listing all accounts
bank.list_accounts()
