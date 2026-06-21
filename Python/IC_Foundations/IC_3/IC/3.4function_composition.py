def compose(*funcs):
    def composed(x):
        result = x
        for func in reversed(funcs):
            result = func(result)
        return result
    return composed

inc = lambda x: x + 1
double = lambda x: x * 2
square = lambda x: x ** 2

f = compose(inc, double, square)

print(f(3))