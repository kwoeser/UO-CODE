# CIS 122 Fall 2020 Assignment 3 Grid
# Author: Karma Woeser
# Partner: Your Partner
# References: 
# Description: Grid problem


def draw_grid(amount):
    """Purpose: Draws a grid of numbers
    This function draws a grid of numbers based on the arguemnt given

    Args: amount is the amount of times the numbers will repeat itself

    Returns: the the ints from 1-3 10 times
    """
    for x in range(amount):
        for i in range(1, 4):
            print(i, end=' ')
        print()


#draw_grid(3)
#draw_grid(6)
draw_grid(10)
