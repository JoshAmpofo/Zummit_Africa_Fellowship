"""
Author: Joshua Ampofo Yentumi

PROBLEM SET 5

Problem 1: Testing my twttr

Description: Reimplement Setting up my twttr from Problem Set 2, restructuring the code per the below
             wherein "shorten" expects a "str" as input and returns that same "str" but with all the vowels
             (A,E, I, O, U) omitted, whether inputted in uppercase or lowercase.
"""


def main():
    text = input("Input text: ").strip()
    print(shorten(text))
    

def shorten(text):
    """Remove all vowels from input text"""
    VOWELS = ['A', 'E', 'I', 'O', 'U']
    

    # create empty string to store new word
    new_word = ""

    # iterate through each character in word
    for char in text:
        if char.upper() not in VOWELS: # check if word is not in vowels list
            new_word += char # form new word
    return new_word


if __name__ == '__main__':
    main()
