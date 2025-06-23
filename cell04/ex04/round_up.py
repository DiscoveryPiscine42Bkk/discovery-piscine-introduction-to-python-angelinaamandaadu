#!/usr/bin/env python3

import math

number_input = input("Give me a number: ")

try:
    number = float(number_input)
    rounded = math.ceil(number)
    print(rounded)
except ValueError:
    print("That is not a valid number.")