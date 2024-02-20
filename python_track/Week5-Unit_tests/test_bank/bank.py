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
    greeting = input("Greeting: ")
    amount = value(greeting)
    print(f"${amount}")


def value(greeting):
    """
    Accepts a greeting from user and outputs a specified amount based on greeting type
    """
    text = greeting.lower().strip()

    if text.startswith("hello") == True:
        return 0
    elif text.startswith("h") and text != "hello":
        return 20
    else:
        return 100


if __name__ == '__main__':
    main()
