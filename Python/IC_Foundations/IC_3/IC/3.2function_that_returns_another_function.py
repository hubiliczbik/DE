def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

def make_validator(min_val, max_val):
    def is_valid(x):
        return min_val <= x <= max_val
    return is_valid

age_validator = make_validator(18,65)


print(double(5))
print(triple(5))
print(double(10))

print(age_validator(18))
print(age_validator(16))




