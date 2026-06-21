class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"Money(amount={self.amount}, currency={self.currency!r})"
    
    def __str__(self):
        if self.currency == "USD":
            return f"${self.amount:.2f}"
        if self.currency == "EUR":
            return f"€{self.amount:.2f}"
        if self.currency == "PLN":
            return f"zł{self.amount:.2f}"
        if self.currency == "JPY":
            return f"JPY {self.amount:.0f}"
        return f"{self.amount} {self.currency}"


usd = Money(99.99, "USD")
eur = Money(50, "EUR")
pln = Money(120.5, "PLN")
jpy = Money(1000, "JPY")

print(str(usd))
print(str(eur))
print(str(pln))
print(str(jpy))

print(repr(usd))
print([usd])      