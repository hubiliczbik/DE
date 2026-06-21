import inspect

def curry(func):
    signature = inspect.signature(func)
    expected_args = len(signature.parameters)

    def curried(*args):
        if len(args) >= expected_args:
            return func(*args)
        
        def next_func(*next_args):
            return curried(*(args + next_args))
        return next_func
    return curried



def add3(a, b, c):
    return a + b + c
curriedAdd = curry(add3)

print(curriedAdd(1)(2)(3))
print(curriedAdd(1, 2)(3))
print(curriedAdd(1)(2, 3))
print(curriedAdd(1, 2, 3))