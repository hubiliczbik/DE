name = input("Enter your name: ")
age = int(input("Enter your age: "))
born_year = int(input("Enter your birth year: "))

klamal = born_year != (2026 - age)

print("Hello", name, "you are", age, "years old.", "Czy klamal?", "Yes" if klamal else "")