class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount * 0.99
    
    def withdraw(self, amount):
        if amount * 1.01 <= self.balance:
            self.balance -= amount * 1.01
            return amount
        else:
            print("Недостаточно средств")
            return 0
    
    def check_balance(self):
        return self.balance

account = BankAccount("12345", "Ivan Ivanov", 1000)
account.deposit(500)
print(account.check_balance()) 
account.withdraw(200)
print(account.check_balance())  
