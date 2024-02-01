def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """check if string fulfills all vanity plate requirements"""

    # Check length
    if len(s) < 2 or len(s) > 6:
        return False

    letters = []
    numbers = []

    # Separate letters and numbers
    for char in s:
        if char.isalpha():
            letters.append(char)
        elif char.isdigit():
            numbers.append(char)

    # Must start with 2 letters
    if len(letters) < 2 or not letters[0].isalpha() or not letters[1].isalpha():
        return False

    # Numbers can only be at the end
    if numbers and letters[-1].isdigit():
        return False

    # No more than 1 number
    if len(numbers) > 1:
        return False

    # First number cannot be 0
    if numbers and numbers[0] == '0':
        return False

    return True


if __name__ == '__main__':
    main()
