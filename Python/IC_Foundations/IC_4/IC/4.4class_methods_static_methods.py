class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_iso(cls, s):
        parts = s.split("-")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        return cls(year, month, day)
    
    @staticmethod
    def is_leap(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"
    
d = Date.from_iso("2026-05-08")

print(d)
print(d.year)
print(d.month)
print(d.day)

print(Date.is_leap(2024))
print(Date.is_leap(2100))

class BusinessDate(Date):
    pass

bd = BusinessDate.from_iso("2026-05-08")

print(bd)
print(type(bd))
