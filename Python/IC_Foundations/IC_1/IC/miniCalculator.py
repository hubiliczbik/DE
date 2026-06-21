def add(a, b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "You cannot divide by 0"
    else:
        return a / b


allowed_operators = ["+", "-", "*", "/"]

while True:
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("What operation do you want? (+,-,*,/)")
        if operator not in allowed_operators:
            print("Invalid operator")
        else:
            second_number = float(input("Enter the second number: "))
            break
    except ValueError:
        print ("Please enter a valid number")

if operator == "+":
    print (add(first_number, second_number))
elif operator == "-":
    print(subtract(first_number, second_number))
elif operator == "*":
    print(multiply(first_number,second_number))
elif operator == "/":
    print(division(first_number, second_number))


 
