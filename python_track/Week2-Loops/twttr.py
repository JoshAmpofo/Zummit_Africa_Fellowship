"""
Author: Joshua Ampofo Yentumi

Problem 3: Just setting up my twttr

Description: Implement a program that prompts the user for a 'str' of text and then
             outputs that same text but with all vowels (A, E, I, O, and U) omitted,
             whether inputted in uppercase or lowercase.
"""


VOWELS = ['A', 'E', 'I', 'O', 'U']


def twttr():
    """Remove all vowels from input text"""

    word = input("Input text: ")
    new_word = ""

    for char in word:
        if char.upper() not in VOWELS:
            new_word += char
    return f"Output: {new_word}"


if __name__ == '__main__':
    print(twttr())
