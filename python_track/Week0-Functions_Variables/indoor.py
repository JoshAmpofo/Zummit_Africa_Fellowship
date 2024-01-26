"""
Author: Joshua Ampofo Yentumi

Problem 1: Indoor Voice

Description: Implement a program in python that prompts the user for input
             and then outputs that same input in lowercase. Punctuation and
             whitespace should be outputted unchanged
"""


def lowercase():
    """
    Converts a string to lowercase
    """
    # obtain uppercase string from user
    sentence = input('Enter uppercase strings: ')
    return sentence.lower()


if __name__ == '__main__':
    print(lowercase())