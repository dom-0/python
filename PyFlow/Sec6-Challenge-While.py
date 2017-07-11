# Guess the number

import random

lowest = 1
highest = 1000
number = random.randint(lowest, highest)

enteredNumber = int(input("Guess the number between {0} and {1}: ".format(lowest, highest)))

while enteredNumber != number:
    if enteredNumber == 0:
        print("Quitting")
        break
    elif enteredNumber > number:
        enteredNumber = int(input("Enter a lower number: "))
    elif enteredNumber < number:
        enteredNumber = int(input("Enter a higher number: "))

else:
    print("You guessed it RIGHT!!!")
