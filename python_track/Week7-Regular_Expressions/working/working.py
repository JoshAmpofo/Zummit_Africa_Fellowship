#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 3: Working 9 to 5

Description: Implement a function called `convert` that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
             Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.
             Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.
              - 9:00 AM to 5:00 PM
              - 9 AM to 5 PM
             Raise a "ValueError" instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).
             But do not assume that someone's hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
"""


import re


def main():
    """run convert program"""
    print(convert(input("Hours: ")))


def convert(s):
    """
    convert 12hr time format to 24hr time format

    Arg(s):
        s (str): time input

    Output:
        Time converted into 24 hr format
    """
    hours = {
        1: 13,
        2: 14,
        3: 15,
        4: 16,
        5: 17,
        6: 18,
        7: 19,
        8: 20,
        9: 21,
        10: 22,
        11: 23,
        12: 00,
    }

    match = re.search(
        r"(.*? AM to .*? PM)|(.*? PM to.*? AM)|(.*? AM to .*? AM)|(.*? PM to .*? PM)", s
    )

    if not match:
        raise ValueError("Invalid input format")

    # AM-PM
    if match.group(1):
        split_group_1 = match.group(1).split()
        first_hour, second_hour = split_group_1[0], split_group_1[3]
        if ":" in first_hour and ":" in second_hour:
            fh_splits, sh_splits = first_hour.split(":"), second_hour.split(":")
            f_hour, f_min, s_hour, s_min = (
                fh_splits[0],
                fh_splits[1],
                sh_splits[0],
                sh_splits[1],
            )
            f_hour, f_min, s_hour, s_min = map(int, [f_hour, f_min, s_hour, s_min])
            if f_hour not in hours or s_hour not in hours:
                raise ValueError("Invalid hour")
            if f_min > 59 or s_min > 59:
                raise ValueError("Invalid time")
            elif f_hour == 12:
                f_hour, s_hour = (0, 12)
                return f"{f_hour:02}:{f_min:02} to {s_hour:02}:{s_min:02}"
            else:
                twenty_four_hour_format = hours[s_hour]
                return (
                    f"{f_hour:02}:{f_min:02} to {twenty_four_hour_format:02}:{s_min:02}"
                )
        else:
            first_hour, second_hour = map(int, [first_hour, second_hour])
            if first_hour not in hours or second_hour not in hours:
                raise ValueError("Invalid hour")
            if first_hour == 12:
                first_hour, second_hour = (0, 12)
                return f"{first_hour:02}:00 to {second_hour:02}:00"
            else:
                twenty_four_hour_format = hours[second_hour]
                return f"{first_hour:02}:00 to {twenty_four_hour_format:02}:00"

    # PM - AM
    elif match.group(2):
        split_group_2 = match.group(2).split()
        first_hour, second_hour = split_group_2[0], split_group_2[3]
        if ":" in first_hour and ":" in second_hour:
            fh_splits, sh_splits = first_hour.split(":"), second_hour.split(":")
            f_hour, f_min, s_hour, s_min = (
                fh_splits[0],
                fh_splits[1],
                sh_splits[0],
                sh_splits[1],
            )
            f_hour, f_min, s_hour, s_min = map(int, [f_hour, f_min, s_hour, s_min])
            tf_fmt = hours[f_hour]
            if f_hour not in hours or s_hour not in hours:
                raise ValueError("Invalid hour")
            if f_min > 59 or s_min > 59:
                raise ValueError("Invalid time")
            elif f_hour == 12:
                f_hour, s_hour = (12, 0)
                return f"{f_hour:02}:{f_min:02} to {s_hour:02}:{s_min:02}"
            elif s_hour == 12:
                s_hour = hours[s_hour]
                return f"{tf_fmt:02}:{f_min:02} to {s_hour:02}:{s_min:02}"
            else:
                return f"{tf_fmt:02}:{f_min:02} to {s_hour:02}:{s_min:02}"
        else:
            first_hour, second_hour = map(int, [first_hour, second_hour])
            if first_hour not in hours or second_hour not in hours:
                raise ValueError("Invalid hour")
            if first_hour == 12:
                first_hour, second_hour = (12, 0)
                return f"{first_hour:02}:00 to {second_hour:02}:00"
            else:
                tfh_fmt = hours[first_hour]
                return f"{tfh_fmt:02}:00 to {second_hour:02}:00"

    # AM-AM
    elif match.group(3):
        split_group_3 = match.group(3).split()
        first_hour, second_hour = split_group_3[0], split_group_3[3]
        if ":" in first_hour and ":" in second_hour:
            fh_splits, sh_splits = first_hour.split(":"), second_hour.split(":")
            f_hour, f_min, s_hour, s_min = (
                fh_splits[0],
                fh_splits[1],
                sh_splits[0],
                sh_splits[1],
            )
            f_hour, f_min, s_hour, s_min = map(int, [f_hour, f_min, s_hour, s_min])
            if f_hour not in hours or s_hour not in hours:
                raise ValueError("Invalid hour")
            if f_min > 59 or s_min > 59:
                raise ValueError("Invalid time")
            elif f_hour and s_hour == 12:
                f_hour, s_hour = (0, 0)
                return f"{f_hour:02}:{f_min:02} to {s_hour:02}:{s_min:02}"
            else:
                return f"{f_hour:02}:{f_min:02} to {s_hour:02}:{s_min:02}"
        else:
            first_hour, second_hour = map(int, [first_hour, second_hour])
            if first_hour not in hours or second_hour not in hours:
                raise ValueError("Invalid hour")
            if first_hour and second_hour == 12:
                first_hour, second_hour = (0, 0)
                return f"{first_hour:02}:00 to {second_hour:02}:00"
            else:
                return f"{first_hour:02}:00 to {second_hour:02}:00"

    # PM-PM
    elif match.group(4):
        split_group_4 = match.group(4).split()
        first_hour, second_hour = split_group_4[0], split_group_4[3]
        if ":" in first_hour and ":" in second_hour:
            fh_splits, sh_splits = first_hour.split(":"), second_hour.split(":")
            f_hour, f_min, s_hour, s_min = (
                fh_splits[0],
                fh_splits[1],
                sh_splits[0],
                sh_splits[1],
            )
            f_hour, f_min, s_hour, s_min = map(int, [f_hour, f_min, s_hour, s_min])
            tfh_fmt_fh, tfh_fmt_sh = hours[f_hour], hours[s_hour]
            if f_hour not in hours or s_hour not in hours:
                raise ValueError("Invalid hour")
            if f_min > 59 or s_min > 59:
                raise ValueError("Invalid time")
            elif s_hour == 12:
                s_hour = 12
                return f"{tfh_fmt_fh:02}:{f_min:02} to {s_hour:02}:{s_min:02}"
            elif f_hour or s_hour:
                return f"{tfh_fmt_fh:02}:{f_min:02} to {tfh_fmt_sh:02}:{s_min:02}"
            elif f_hour and s_hour == 12:
                f_hour, s_hour = (12, 12)
                return f"{f_hour:02}:{f_min:02} to {s_hour:02}:{s_min:02}"

        else:
            first_hour, second_hour = map(int, [first_hour, second_hour])
            if first_hour not in hours or second_hour not in hours:
                raise ValueError("Invalid hour")
            if first_hour == 12:
                first_hour = 12
                return f"{first_hour:02}:00 to {hours[second_hour]:02}:00"
            elif first_hour or second_hour:
                tfh_fmt_fh, tfh_fmt_sh = hours[first_hour], hours[second_hour]
                return f"{tfh_fmt_fh:02}:00 to {tfh_fmt_sh:02}:00"


if __name__ == "__main__":
    main()
