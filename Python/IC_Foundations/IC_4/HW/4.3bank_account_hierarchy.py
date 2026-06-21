class InsufficientFundsError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class UnauthorizedError(Exception):
    pass

class Account:
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance
        
    
    @property
    def owner(self):
        return self._owner
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <=0:
            raise InvalidAmountError("Amount must be positive")
        self._balance = self._balance + amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("The amount exceeds the available balance")
        self._balance = self._balance - amount

    
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return interest

class CheckingAccount(Account):
    def __init__(self, owner, balance, overdraft_limit = 0):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            raise ValueError ("You cannot withdraw the amount of cash")
        self._balance -= amount

class JointAccount(Account):
    def __init__(self, owners, balance=0):
        super().__init__(owners, balance)
    
    def withdraw(self, amount, owner):
       if owner not in self.owner:
            raise UnauthorizedError("Owner is not allowed to withdraw")
       else:
           super().withdraw(amount)

s = SavingsAccount("Anna", 1000, interest_rate=0.05)
s.apply_interest()
print(s.balance) 

c = CheckingAccount("Piotr", 100, overdraft_limit=200)
c.withdraw(250)
print(c.balance)

j = JointAccount(["Anna", "Piotr"], 500)
j.withdraw(100, owner="Anna")
print(j.balance) 

j.withdraw(100, owner="Bob")
    
    


