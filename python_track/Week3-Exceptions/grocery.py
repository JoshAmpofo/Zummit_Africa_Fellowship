"""
Author: Joshua Ampofo Yentumi

Problem 3: Grocery List

Description: Implement a program that prompts the user for items, one per line
             until the user inputs control-d. Then output the user's grocery list in all uppercase,
             sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
             No need to pluralize the items. Treat the user's input case-insensitively.
"""


def grocery_list():
    """
    Create a grocery list based on user input Nd return number of times user enters
    an item.
    """

    # create grocery dictionary
    grocery_dict = {}
    try:
        # set infinite loop
        while True:
            # obtain user input
            item = input().lower()
            # add items to dictionary
            if item in grocery_dict:
                grocery_dict[item] += 1 # increase count if key exists already
            else:
                grocery_dict[item] = 1 # set count to one if key doesn't exist
    except EOFError:
        # sort dict by key and format output
        for item, count in sorted(grocery_dict.items()):
            print(f'{count} {item.upper()}')


if __name__ == "__main__":
    grocery_list()
