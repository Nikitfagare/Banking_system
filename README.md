# Banking System in Python

## Description
This project is a basic Banking System built using Object-Oriented Programming (OOP) concepts in Python. It shows how classes and objects can be used to model real-world banking operations. The system supports account creation, deposits, withdrawals, interest calculation, overdraft handling, and fund transfers between accounts.

## Features
- Create Savings and Current accounts with unique account numbers  
- Deposit and withdraw money with proper validation  
- Savings accounts can calculate and add interest  
- Current accounts support overdraft up to a limit  
- Transfer funds between accounts  
- Bank class manages multiple accounts  

## OOP Concepts Used
- Encapsulation: private attributes with controlled access methods  
- Inheritance: SavingsAccount and CurrentAccount extend the base Account class  
- Polymorphism: withdraw method behaves differently depending on account type  
- Abstraction: common operations defined in Account, specialized in subclasses  
- Composition: Bank class manages multiple Account objects  

## Example Usage
```python
bank = Bank("My Bank")

savings = SavingsAccount("S001", "Nikit", 1000)
current = CurrentAccount("C001", "Alex", 500)

bank.add_account(savings)
bank.add_account(current)

print(savings.deposit(200))
print(savings.add_interest())
print(current.withdraw(800))
print(bank.transfer("S001", "C001", 300))
```

## Future Improvements
- Add a simple menu-driven interface for user interaction  
- Implement transaction history and account statements  
- Add authentication and security features  
- Extend with more account types like Fixed Deposit or Loan Accounts  

