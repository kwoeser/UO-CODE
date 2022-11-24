# CIS 122 Fall 2020 Lab 2 Pythgorean 
# Author: Karma Woeser
# Partner: Your Partner
# References: https://www.rapidtables.com/calc/math/pythagorean-calculator.html
# Description: Pythagorean problem

import math

def calc_side_c(a, b):
    # Uses the pow syntax to square a and b, then it adds them
    c_squared = pow(a, 2) + pow(b, 2)
    # Finds the square root of c_squared and returns c rounded to the second decimal point
    c = math.sqrt(c_squared)
    return round(c, 2)

# Calculate missing side c
print('c =', calc_side_c (5, 10))


def calc_side_ab(a, c):
    # Uses the pow syntax to square a and b, then it subtracts them
    b_squared = pow(c, 2) - pow(a, 2)
    b = math.sqrt(b_squared)
    return round(b, 2)

# Calculate missing side a or b
print('b = ', calc_side_ab (4, 8))
