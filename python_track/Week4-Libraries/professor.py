#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 5: Little Professor

Description: Implement a program that:
             - Prompts the user for a level,
             - If the user does not input 1, 2, or 3, the program should prompt again.
             - Randomly generates ten (10) math problems formatted as "X + Y = ",
                wherein each of X and Y is a non-negative integer with digits. No need to support operations other than addition (+).
            - Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
              the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem.
              If the user has still not answered correctly after three tries, the program should output the correct answer.
            - The program should ultimately output the user's score: the number of correct answers out of 10.
            - Structure the program as follows,
                - wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3,
                - and generate_integer returns a randomly generated non-negative integer with level digits
                - or raises a ValueError if level is not 1, 2, or 3:
"""

import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        answer = x + y
        for attempt in range(3):
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(answer)
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except ValueError:
            pass

def generate_integer(level):
    return random.randint(0 if level == 1 else 10 ** (level - 1), 10 ** level - 1)

if __name__ == "__main__":
    main()
