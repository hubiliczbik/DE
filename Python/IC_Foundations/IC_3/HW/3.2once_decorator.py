from functools import wraps

def once(func):
    has_run = False
    result = None

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal has_run, result
        if not has_run:
            result = func(*args, **kwargs)
            has_run = True
        return result

    return wrapper


@once
def init_db():
    print("connecting...")
    return "connection_id_42"

print(init_db()) 
print(init_db()) 
print(init_db())