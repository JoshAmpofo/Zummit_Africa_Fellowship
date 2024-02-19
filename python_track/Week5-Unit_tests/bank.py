"""
Author: Joshua Ampofo Yentumi

Problem 2: Back to the Bank

Description: Re-implement Home Federal Savings Bank from Problem Set 1.
             restructuring the code per the below, wherein ```value``` expects a ```str``` as input and returns
             an ```int```, namely 0 if that str starts with "hello", 20 if that str starts with an "h" (but not "hello"),
             or 100 otherwise, treating the str case-insentively.
             Assume that the string passed to the ```value``` function will not contain any leading spaces.
             Only "main" should call ```print```
"""


def main():
    # take input from user and return appropriate output
    message = input("Greeting: ").lower().strip()
    amount = value(message)
    print(f"${amount}")


def value(greeting):
    """
    Accepts a greeting from user and outputs a specified amount based on greeting type
    """
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h") and greeting != "hello":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
