def tokenize(expression):
    tokens = []
    for char in expression:
        print(char)
        if char == "+" or char == "-" or char == "*" or char == "/":
            tokens.append(char)
        if char.isdigit():
            tokens.append(int(char))
        if char == "(" or char == ")":
            tokens.append(char)
        if char == " ":
            continue
    return tokens