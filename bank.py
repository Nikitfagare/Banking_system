Banking system

class Account:
    def __init__(self, account_number, owner, balance=0):
        self._account_number = account_number   # encapsulated attributes
        self._owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited {amount}. New balance: {self._balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        return "Insufficient funds"

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account({self._account_number}, Owner: {self._owner}, Balance: {self._balance})"


class SavingsAccount(Account):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.05):
        super().__init__(account_number, owner, balance)
        self._interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self._interest_rate
        self._balance += interest
        return f"Interest added: {interest}. New balance: {self._balance}"


class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance=0, overdraft_limit=500):
        super().__init__(account_number, owner, balance)
        self._overdraft_limit = overdraft_limit

    def withdraw(self, amount):  # polymorphism (method overriding)
        if 0 < amount <= self._balance + self._overdraft_limit:
            self._balance -= amount
            return f"Withdrew {amount}. New balance: {self._balance}"
        return "Overdraft limit exceeded"


class Bank:
    def __init__(self, name):
        self._name = name
        self._accounts = {}

    def add_account(self, account):
        self._accounts[account._account_number] = account
        return f"Account {account._account_number} added."

    def get_account(self, account_number):
        return self._accounts.get(account_number, "Account not found")

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if isinstance(sender, Account) and isinstance(receiver, Account):
            withdraw_msg = sender.withdraw(amount)
            if "Withdrew" in withdraw_msg:
                receiver.deposit(amount)
                return f"Transferred {amount} from {from_acc} to {to_acc}"
            return withdraw_msg
        return "Invalid account(s)"

    def __str__(self):
        return f"Bank({self._name}, Accounts: {len(self._accounts)})"


# ------------------- USAGE -------------------
bank = Bank("Nikit Bank")

# Create accounts
savings = SavingsAccount("S001", "Nikit", 1000)
current = CurrentAccount("C001", "Alex", 500)

# Add accounts to bank
print(bank.add_account(savings))
print(bank.add_account(current))

# Transactions
print(savings.deposit(200))
print(savings.add_interest())
print(current.withdraw(800))   # overdraft allowed
print(current.withdraw(1000))  # overdraft exceeded

# Transfer
print(bank.transfer("S001", "C001", 300))

# Check balances
print(savings.get_balance())
print(current.get_balance())
