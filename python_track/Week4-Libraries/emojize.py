#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

PROBLEM SET 4

Problem 1: Emojize

Description: Implement a program that prompts a user for a "str" in English
             and then outputs the "emojized" version of that "str", converting
             any codes (or aliases) therein to their corresponding emoji
"""

import emoji


def main():
    """Runs a text to emoji function"""

    # obtain user input
    text = input("Enter a text: ")
    # run text-to-emoji fuxn on input text
    convert_to_emoji(text)


def convert_to_emoji(text):
    """Convert a text input containing unicode to appropriate emoji"""
    # convert text to emoji
    print(emoji.emojize(text, language='alias'))  # enable full list of emoji with language='alias'


if __name__ == "__main__":
    main()
