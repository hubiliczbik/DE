from functools import wraps
def add(a, b = 42):
    return a + b

def sub(func):
    return func(1)

print(sub(func=add))


def audited(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


