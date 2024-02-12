#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 4: Guessing Game

Description: Implement a program that:
             - Prompts the user for a level, "n". If the user does not input a positive integer, the program should prompt again.
             - Randomly generates an integer between 1 and n, inclusive, using the "random" module.
             - Prompts the user to guess that integer. If guess is not a positive integer, the program should prompt the user again.
                o If the guess is smaller than that integer, the program should output "Too small!" and prompt the user again.
                o If the guess is larger than that integer, the program should output "Too large!" and prompt again the user again.
                o If the guess is the same as that integer, the program should output "Just right!" and exit.
"""

from random import randint
import sys


def main():
    # allow any positive integer including 1
    number = get_positive_integer("Level: ", allow_zero=False)
    answer = randint(1, number)

    while True:
        # check if level is 1, allow 0 as a guess
        allow_zero_guess = (number == 1)
        guess = get_positive_integer("Guess: ", allow_zero=allow_zero_guess)
        
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit(0)


def get_positive_integer(prompt, allow_zero):
    """check if user input is a positive integer or not"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0 or (allow_zero and value == 0):
                return value
            else:
                pass
        except ValueError:
            pass


if __name__ == "__main__":
    main()