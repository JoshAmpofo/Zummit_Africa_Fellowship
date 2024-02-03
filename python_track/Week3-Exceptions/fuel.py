"""
Author: Joshua Ampofo Yentumi

PROBLEM SET 3

Problem 1: Fuel Gauge

Description: In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
             and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
             If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
             And if 99% or more remains, output F instead to indicate that the tank is essentially full.

             If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.)
             Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""


def gauge():
    """Prints out the fuel percentage level"""
    while True:
        # obtain user input and split into X and Y
        try:
            x, y = map(int, input("Fraction: ").split("/"))
            
            # check if X is greater than Y or Y is 0
            if x > y or y == 0:
                continue
            
            # calculate fuel percentage and return output based on fuel level
            result = (x / y) * 100

            if result <= 1:
                return "E"
            elif result >= 99:
                return "F"
            else:
                return f"{result:.0f}%"
        # catch non-integer values and division by zero
        except (ValueError, ZeroDivisionError):
            continue
            

if __name__ == "__main__":
    print(gauge())
