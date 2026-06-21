def add_to(value, target=[]):
    target.append(value)
    return target
print(add_to(1))
print(add_to(2))
print(add_to(3))

"None as default value, because mutable defaults ale reated only when the function is definied"


def add_t1(value, target=None):
    if target is None:
        target = []
    target.append(value)
    return target
print(add_t1(1))
print(add_t1(2))
print(add_t1(3))
