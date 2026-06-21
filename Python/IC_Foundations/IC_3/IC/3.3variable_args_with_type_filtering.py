def sum_numeric(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
    return total

print(sum_numeric(1, 2, 3))
print(sum_numeric(1, "two", 3.0, None))
print(sum_numeric)
