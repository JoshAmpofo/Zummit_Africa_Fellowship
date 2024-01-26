"""
Author: Joshua Ampofo Yentumi

Problem 4: Einstein Energy Equation

Description: Implement a python program that prompts a user for mass as an integer (in kilograms)
             and then outputs the equivalent number of joules as an integer. Assume that the user
             will input an integer.
"""

# Speed of light constant
c = 300000000


def energy():
    """Calculates the number of joules using the Einstein equation E = mcsquared"""
    # ask user for mass input
    m = int(input('m: '))

    # calculate energy produced by mass
    E = m * pow(c, 2)

    return f'E: {int(E)}'


if __name__ == '__main__':
    print(energy())
