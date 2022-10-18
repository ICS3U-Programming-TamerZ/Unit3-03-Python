#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Oct. 5, 2022
# This program checks if the user guessed a number correctly
# using an If.. Then.. Else statement.

import random


def main():

    # Assigns a random number from 0-9 to the number variable.
    number = random.randint(0, 9)

    # Asks the user's for their guess.
    print("The secret number is within the range of 0-9")
    user_guess = float(input("Enter your guess: "))

    # Code shows if the user guessed correctly.
    if number == user_guess:
        print("You guessed correctly!")

    # Code shows if the user guessed incorrectly.
    else:
        print("You guessed incorrectly. The correct answer was {number}")


if __name__ == "__main__":
    main()
