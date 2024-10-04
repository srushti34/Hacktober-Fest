class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funds')

account = BankAccount('Alice', 1000)
account.deposit(500)
account.withdraw(200)
print(account.balance())