"""
Author: Joshua Ampofo Yentumi

Problem 4: Outdated

Description: Implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
             wherein the month in the latter might be any of the values in the list below:
             [
                 "January",
                 "February",
                 "March",
                 "April",
                 "May",
                 "June",
                 "July",
                 "August",
                 "September",
                 "October",
                 "November",
                 "December"
        ].
        Then output that same date in YYYY-MM-DD format.
        If the user’s input is not a valid date in either format, prompt the user again.
        Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""


def date():
    """
    Prompts a user for a date in the format MM/DD/YYYY and format input as YYYY-MM-DD.
    """
    months = [
        "January",
        "February",
        "March",
        "April",
        "May", 
        "June", 
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]

    # set infinit loop
    while True:
        # obtain user input
        user_date = input("Date: ").strip()
        # check if user_input is in this format (MM/DD/YYYY)
        if "/" in user_date:
            parts = user_date.split("/")
            # check if length of parts is 3 and all digits
            if len(parts) == 3 and all(part.isdigit() for part in parts):
                # assign parts to month, date and year
                month, day, year = parts
                if int(month) > 12 or int(day) > 31: # wrong date input check
                    continue
                print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
                break

        # check if user input is in the MM DD, YYYY format
        elif "," in user_date:
            parts = user_date.replace(",", "").split()
            # check for individual date items
            if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
                if parts[0] not in months or int(parts[1]) > 31:  # wrong date input check
                    continue
                # execute try block
                try:
                    # check month list by indexing from 1
                    month_index = months.index(parts[0]) + 1
                    print(f"{parts[2]}-{str(month_index).zfill(2)}-{parts[1].zfill(2)}")
                    break
                except ValueError:
                    pass


if __name__ == "__main__":
    date()

