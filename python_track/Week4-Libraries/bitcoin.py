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

import requests
import sys

# Error checks
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    num_bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# get price index
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # error checking for request
    response.raise_for_status() # HTTPError catch
except requests.RequestException as e:
    sys.exit(f"Request Error: {e}")

# calculate bitcoin price
try:
    response_json = response.json()
    current_price_usd = response_json['bpi']['USD']['rate_float']
    total_price = current_price_usd * num_bitcoins
    print(f"${total_price:.4f}")
except (KeyError, ValueError, TypeError) as e:
    sys.exit(f"Error: {e}")
