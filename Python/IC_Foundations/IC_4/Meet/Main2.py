from abc import ABC, abstractmethod

class GierekError(Exception):
    pass


class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self.currency = currency
    
    def convert_to_usd(self):
        return self._amount / 3.4
    
    def __repr__(self):
        return f"Money({self._amount}, {self.currency})"
    
    @classmethod
    def from_usd(cls, money):
        return Money(money._amount * 3.4, "pln")
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        raise GierekError("Nie wolno zmieniać wartości pieniędzy")


        


money_pln = Money(3, "PLN")
money_pln.amount = 50


money_will_be = Money(2, "USD")

print(money_pln)
print(money_pln.convert_to_usd())
print(Money.from_usd(money_will_be))


class Banknote(Money, ABC):
    def __init__(self, amount, currency, serial_number):
        super().__init__(amount, currency)
        self.serial_number = serial_number
    
    def __repr__(self):
        return f"Banknote({self._amount}, {self.currency}, {self.serial_number})"
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        raise GierekError("Nie wolno zmieniać wartości banknotu")

class PaperBanknote(Banknote):
    def __init__(self, amount, currency, serial_number, year):
        super().__init__(amount, currency, serial_number)
        self.year = year
    
    def __repr__(self):
        return f"PaperBanknote({self._amount}, {self.currency}, {self.serial_number}, {self.year})"
    
    @abstractmethod
    def burn():
        pass