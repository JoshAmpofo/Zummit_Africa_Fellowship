"""
Author: Joshua Ampofo Yentumi

Problem 2: Felipe's Taqueria

Description: Implement a program taht enables a user to place an order, prompting them for items
             one per line, until the user inputs control-d (common way of ending one's input to a program).
             After eaxh inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($)
             and formatted to two decimal places. Treaat the user's input case insensitively.
             Ignore any input that isn't an item. Assume every item on the menu will be titlecased.
"""


def diner_order():
    """Takes an order from a diner menu and calculates the total price"""

    # define diner menu
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # intialize total_price variable
    total_price = 0

    # execute try block
    try:
        # set infinite loop
        while True:
            # obtain user input
            order = input("Item (ctrl+D to quit): ").title()

            # break if input is empty
            if order == "":
                break

            # check if input is a key in dictionary
            for item in menu:
                if item == order: # if item is in dictionary,
                    total_price += menu.get(item) # add price of item to total_price
                    print(f'Total: ${total_price:.2f}')

    # execute except block
    except EOFError:
        print(f'Total: ${total_price:.2f}')


if __name__ == "__main__":
    diner_order()
