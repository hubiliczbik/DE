import random

while True:
    try:
        how_number = int(input("How many numbers are to draw?"))
        max_number = int(input("Max number?"))
        if how_number <= 0 or max_number < how_number:
            print("Impossible to draw without repetition")
        else:
            winNumber = (random.sample(range(1, max_number + 1), how_number))
            print("Winning number: ", (sorted(winNumber)))
            answer = input("Do you want to play again? (y/n)")
            if answer.lower() == "n":
                break
    except ValueError:
        print("Please enter valid numbers")




