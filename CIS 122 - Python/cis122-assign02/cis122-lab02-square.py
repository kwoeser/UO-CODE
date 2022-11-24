# CIS 122 Fall 2020 Lab 2
# Author: Karma Woeser
# Partner: Your Partner
# Description: Create a function that returns the square of any positive integer


# Step 1: Define a function that accepts a number
def square(num):
     # Multiplies num by num and returns the result
     return num * num

# Test
print(str(square(2)) + ', ' + str(square(10)) + ', ' + str(square(100)))
print("2 squared is",square(2))
print("10 squared is",square(10))
print("100 squared is",square(100))
