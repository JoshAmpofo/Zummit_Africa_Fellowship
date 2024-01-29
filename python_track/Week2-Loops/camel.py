"""
Author: Joshua Ampofo Yentumi

Problem Set 2

Problem 1: camelCase

Description: Implement a program that prompts the user for the name of a variable in camelCase.
             The output of the corresponding name should be in snake_case.
             Assume that the user's input will indeed be in camel case.
"""


def snake_case():
    """Convert user input (in camelCase) to snake_case"""
    # prompt user for input
    user_input = input("Enter word (in camelCase) preferably: ")
    
    # convert camelCase to snake_case
    snake_case_char_list = ['_' + char.lower() if char.isupper() else char for char in user_input]
    
    return ''.join(snake_case_char_list).strip('_')


if __name__ == '__main__':
    print(snake_case())