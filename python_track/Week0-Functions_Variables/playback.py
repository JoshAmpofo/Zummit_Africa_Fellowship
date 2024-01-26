"""
Author: Joshua Ampofo Yentumi

Problem 2: Playback Speed

Description: Implement a python program that prompts a user
             for input and then outputs the same input, replacing
             each space with three periods (...)
"""


def playback():
    """
    Takes a string and replaces spaces with three periods
    """
    # obtain input from user
    sentence = input('Enter a sentence: ')
    # split strings into individual words
    words = sentence.split()
    # join words with '...' separator
    return '...'.join(words)


if __name__ == '__main__':
    print(playback())
