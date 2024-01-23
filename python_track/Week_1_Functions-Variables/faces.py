""""
Author: Joshua Ampofo Yentumi

Problem 3: Making Faces

Description: Implement a function that accepts a str as input and returns the same input
             with any :) converted to "🙂" (slightly smiling face) and any :( converted
             to "🙁" (slightly frowning face). All other text should be returned unchanged.
             In the same file, implement a function called "main" that prompts the user for input,
             calls convert on that input, and prints the result.
"""


def convert(text: str) -> str:
    """Replace specific emoticons with emoji in a sentence"""
    text = text.replace(':)', '🙂').replace(':(', '🙁')
    return text


def main():
    """Converts a sentence with emoticons into an emoji included sentence"""
    sentence = input('Enter a sentence with happy or sad string emoticon: ')
    emojified_sentence = convert(sentence)
    return emojified_sentence


if __name__ == '__main__':
    print(main())
