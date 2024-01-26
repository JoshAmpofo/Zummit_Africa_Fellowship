"""
Author: Joshua Ampofo Yentumi
PROBLEM SET 1
Problem 1: Deep Thought

Description: Implement a program that prompts a user for the answer to the Great
             Question of Life, the Universe and Everything, outputting "YES" if
             the user inputs "42" or (case-insensitively) "forty-two" or "forty two".
             Otherwise output "NO".
"""


def great_question():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    match answer.lower().strip():
        case '42' | 'forty-two' | 'forty two':
            return 'Yes'
        case _:
            return "No"


if __name__ == '__main__':
    print(great_question())