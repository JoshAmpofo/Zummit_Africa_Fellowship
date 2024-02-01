"""
Author: Joshua Ampofo Yentumi

Problem 5: Nutrition Facts

Description: Implement a program that prompts a user to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit,
             per the US FDA's poster for fruits.
             Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry).
             Ignore any input that isn't a fruit.
"""


def nutrition_facts():
    """Provides nutritional facts of fruits as per US FDA recommendations"""

    # create fruit dictionary
    fruits = {
        "apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60,
        "grapes": 90, "honeydew melon": 50, "kiwifruit": 90, "lemon": 15, "lime": 20,
        "nectarine": 60, "orange": 80, "peach": 60, "pear": 100, "pineapple": 50,
        "plums": 70, "strawberries": 50, "sweet cherries": 100, "tangerine": 50, "watermelon": 80
    }

    #  get user input
    fruit_search = input("Item: ").lower()

    # search dictionary for fruit nutritional information
    for fruit in fruits:
        if fruit == fruit_search:
            print(f"Calories: {fruits[fruit]}")



if __name__ == "__main__":
    nutrition_facts()
