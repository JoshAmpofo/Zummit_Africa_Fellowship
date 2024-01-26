"""
Author: Joshua Ampofo Yentumi

Problem 2: Home Federal Savings Bank

Description: Implement a program that prompts the user for a greeting.
             If the greeting starts with "hello", output "$0".
             If the greeting starts with an "h" (but not "hello"), output "$20".
             Otherwise, output "$100". Ignore any leading whitespace in the user's greeting, and treat the user's greeting case-insensitively.
"""


def main():
    # take input from user and return appropriate output
    message = input("Greeting: ").lower().strip()
    return greeting(message)


def greeting(txt):
    """
    Accepts a greeting from user and outputs a specified amount based on greeting type
    """
    if txt.startswith("hello"):
        return "$0"
    elif txt.startswith("h") and txt != "hello":
        return "$20"
    else:
        return "$100"


if __name__ == '__main__':
    print(main())