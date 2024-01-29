"""
Author: Joshua Ampofo Yentumi

Problem 2: Coke Machine

Description: Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents
             and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

             Implement a program that prompts the user to insert a coin, one at a time,
             each time informing the user of the amount due. Once the user has inputted 50 cents,
             output how many cents in change the user is owed. Assume that the user will only input integers
             and ignore any integer that isn't an accepted denomination.
"""

DENOMS = [25, 10, 5]
AMOUNT = 50

print(f"Amount Due: {AMOUNT}")

# keep track of amount entered
TOTAL_AMOUNT = 0

while True:
    # get user input
    amount = int(input("Insert Coin: "))

    # check if amount entered is in denom list
    if amount in DENOMS:
        # update TOTAL_AMOUNT
        TOTAL_AMOUNT += amount

    # check if amount is exactly up to actual amount of coke
    if TOTAL_AMOUNT == AMOUNT:
        zero_balance = TOTAL_AMOUNT - AMOUNT
        print(f"Change Owed: {zero_balance}")
        break

    # check for overpayment
    elif TOTAL_AMOUNT > AMOUNT:
        change_owed = TOTAL_AMOUNT - AMOUNT
        print(f"Change Owed: {change_owed}")
        break

    else:
        amount_due = AMOUNT - TOTAL_AMOUNT
        print(f"Amount Due: {amount_due}")
