def score(password):
    score = 0
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    length = len(password)
    for char in password:
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
        if not char.isalnum():
            has_special = True
    if has_lower:
        score += 10
    if has_upper:
        score += 10
    if has_digit:
        score += 10
    if has_special:
        score += 20
    if length >= 8:
        score += 20
    if length >= 12:
        score += 10
    if length >= 16:
        score += 10
    if password == "password" or password == "123456" or password == "qwerty":
        score = 0
    return score