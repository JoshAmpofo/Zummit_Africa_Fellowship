#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 4: Regular, um, Expressions

Description: Implement a function called `count` that expects a line of text as input as a str and returns, as an int, the number of times that “um” appears in that text, 
             case-insensitively, as a word unto itself, not as a substring of some other word. 
             For instance, given text like "hello, um, world", the function should return 1. 
             Given text like yummy, though, the function should return 0.
"""

import re


def main():
    """run count program"""
    print(count(input("Text: ")))


def count(s):
    """
    count the number of times the word `um` appears in a str as a word not a substring

    Arg(s):
        s (str): target str to search for word

    Return:
        (int): number of times word appears
    """
    match = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(match) if match else 0


if __name__ == "__main__":
    main()
