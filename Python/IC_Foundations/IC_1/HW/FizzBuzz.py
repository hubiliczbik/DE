numbers = [15,21,35,105,8]

for i in numbers:
    result = ""

    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result += "Buzz"
    if i % 7 == 0:
        result += "Bang"
    if result == "":
        print(i)
    else:
        print(result)