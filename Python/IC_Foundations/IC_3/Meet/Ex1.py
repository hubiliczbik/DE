def compose(*functions):
    def inner(x):
        for f in reversed(functions):
            x = f(x)
        return x
    return inner




inc = lambda x: x + 1
double = lambda x: x * 2
square = lambda x: x ** 2

f = compose(inc, double, square)
print(f(3))
