
def czy_bliskie(a: float, b: float) -> bool:
    return abs(b - a) < 1e-9


print(czy_bliskie(0.3, 0.1 + 0.2))