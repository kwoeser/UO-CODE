# CIS 122 Fall 2021 Assignment 3 Circle
# Author: Karma Woeser
# Partner: Your Partner
# References: 
# Description: Reverse words problem


def reverse(string, new_string):
    """Purpose: Reverse the string
    This function reverses a string by using a for loop where i holds everything in the
    original string. Then adds i (each letter) with new_string.

    Args: string is the string that is going to be reversed
    new_string is the an blank string that will have the new reversed string added to it

    Returns: the reversed string
    """
    
    print ("Original: " + string)
    for i in string:
        new_string = i + new_string
    return new_string

print("Reversed: " + reverse("When in the course of human events", ''))


t = 'racecar'
print(t[::1])



f = 'ronald'
print(f[::1])

