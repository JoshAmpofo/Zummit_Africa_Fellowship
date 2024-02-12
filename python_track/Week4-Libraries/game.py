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
    """Guess a number game"""
    # accept all positive integers starting from 1
    level = get_int("Level: ", min_val=1)
    answer = randint(1, level)

    while True:
        # get guess number, accept 0 as guess if level is 1
        guess = get_int("Guess: ", min_val=0 if level == 1 else 1)
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit(0)


def get_int(prompt, min_val):
    """Prompt for an integer with a minimum value, reprompting on invalid input."""
    while True:
        try:
            value = int(input(prompt))
            if value >= min_val:
                return value
            else:
                pass
        except ValueError:
            pass


if __name__ == "__main__":
    main()
