"""
Author: Joshua Ampofo Yentumi

Problem 5: Meal Time

Description: Implement a program that prompts the user for a time and outputs whether
             it's "breakfast time", "lunch time", or "dinner time". If it's not time for a meal,
             don't output anything at all. Assume that the user's input will be formatted in 24-hour format
             time as "#:##" or "##:##". Assume that each meal's time range is inclusive.
             For instance, whether it's 7:00, 7:01, 7:59, or 8:00, or anytime between, it's time for breakfast.
             Breakfast: 7:00 - 8:00
             Lunch: 12:00 - 13:00
             Dinner: 18:00 - 19:00
"""


def main():
    time = input("What time is it? ")
    result = convert(time)

    if 18.0 <= result <= 19.0:
        return "dinner time"
    elif 12.0 <= result <= 13.0:
        return "lunch time"
    elif 7.0 <= result <= 8.0:
        return "breakfast time"
    else:
        return None

def convert(time):
    hours, minutes = time.split(":")
    # convert hours to float
    hours = float(hours)
    # convert minutes into fraction of an hour
    fract_minutes = float(minutes) / 60
    # obtain total time
    time = hours + fract_minutes
    return time


if __name__ == "__main__":
    print(main())
