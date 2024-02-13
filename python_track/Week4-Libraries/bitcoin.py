#!/usr/bin/env python3

"""
Author: Joshua Ampofo Yentumi

Problem 6: Bitcoin Price Index

Description: Implement a program that:
             - Expects the user to specify as a command-line argument the number of Bitcoins, n, that they would like to buy.
             - If that argument cannot be converted to a "float", the program should exit via "sys.exit" with an error message.
             - Queries the API for the CoinDesk Bitcoin Price Index at "https://api.coindesk.com/v1/bpi/currentprice.json",
                which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
             - Catch any exceptions as appropriate
"""

import json
import requests
import sys


def main():
    """run logic for bitcoin price checker program"""
    num_bitcoins = get_num_bitcoins()
    current_price_usd = get_bitcoin_price()
    total_amount = calculate_price(num_bitcoins, current_price_usd)
    print(f"$ {total_amount:.4f}")


def get_num_bitcoins():
    """Retrieves the number of bitcoins to check amount in USD"""
    # Error checks
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_bitcoin_price():
    """get bitcoin price in USD based on number of coins inputted by user"""

    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    # get price index
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTPError catch
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    # error checking for request
    except requests.RequestException as e:
        sys.exit(f"Request Error: {e}")
    except (KeyError, ValueError, TypeError) as e:
        sys.exit(f"Error: {e}")


def calculate_price(num_bitcoins, price_per_bitcoin):
    """
    Calculates the total price for a given number of bitcoins
    """
    return num_bitcoins * price_per_bitcoin


if __name__ == "__main__":
    main()
