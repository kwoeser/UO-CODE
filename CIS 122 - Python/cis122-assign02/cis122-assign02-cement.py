# CIS 122 Fall 2020 Lab 2 Cement
# Author: Karma Woeser
# Partner: Your Partner
# References: https://www.concretenetwork.com/concrete/howmuch/calculator.htm
# References: https://todayshomeowner.com/cubic-yard-calculator/
#Description: Cement problem

import math 

def calc_yards_cement(t,w,l):
    # Multiplies length times width, then multiplies the result of the by thickness/12
    cubic_feet = l * w * (t / 12)
    
    # The result from above is divided by 27; dividing by 27 makes cubic feet into cubic yards
    cubic_yards = cubic_feet / 27
    
    # Rounds cubic_yards to the second decimal point and returns the result
    return round(cubic_yards, 2)


def print_results(t,w,l):
    # Converts the width and length to inches by multipling by 12
    width_in_inches = w *12
    length_in_inches = l * 12
    
    
    # String concatnation 
    string = "A cement slab " + str(t) + '" thick, ' + str(width_in_inches)
    string_two = '" wide and ' + str(length_in_inches)
    string_three = '" long requires ' + str(calc_yards_cement(t,w,l)) + " cubic yards of cement."

    print(string + string_two + string_three)

print_results(4,6,10)
print_results(4,10,20)


