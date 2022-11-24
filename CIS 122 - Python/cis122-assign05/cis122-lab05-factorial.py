# CIS 122 Fall 2020 Lab 5 Factorial
# Author: Karma Woeser
# Partner: Your Partner
# References:
# Description: Factorial problem


def factorial(num):
    """Purpose: To calculate the factorial of an integer


    Args: num is number which factorial will be found.

    Returns: Returns False if the integer is >= 0. Returns 1 if the integer is == 0. When
    the integer is >= 1 it will run a loop through 1 and the integer inputed + 1. Then it will
    multiply the total (1) by i which will depend on what the integer inputed is. The result
    of total is returned
    """
    if num < 0:
        print("Must be >= 0")
        return False
    elif num == 0:
        return 1
    total = 1
    number = num + 1
    if num >= 1:
        for i in range(1, number):
            total = total * i
        return total

enter_num = int(input("Enter factorial number: "))
print(factorial(enter_num))

#print(factorial(5))
#factorial(-1)
#factorial(0)

'''
import math

def test_factorial(num):
    errors = 0
    range_num = num + 1
    fact = factorial(num)
    fact_two = math.factorial(fact)
    if fact_two != fact:
        print("Errors", num,": errors")
    elif fact_two == fact:
        print("Correct")

    enter_num = int(input("Enter factorial number: "))
    print(fact)

test_factorial(5)
#test_factorial(enter_num)
'''
