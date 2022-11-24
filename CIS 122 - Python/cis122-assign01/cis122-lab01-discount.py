''' 
CIS 122 Fall 2021 Lab 1 Challenge
Author: Karma Woeser
Credit: 
Description: Lab 1 discount 
'''

# Sets the variables and finds the type of object
cost = 50
type(cost)
discount = 0.10
type(discount)

# Multiplies the -cost by discount then adds cost to that and sets the outcome of that to an variable
discounted_cost = cost - cost * discount
#print(discounted_cost)

# Prints "Discounted Cost:" and the variable discounted_cost
discounted_label = 'Discounted cost:'
print(discounted_label, discounted_cost)


