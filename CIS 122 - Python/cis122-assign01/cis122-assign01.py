# CIS 122 Fall 2021 Assignment 1 
# Author: Karma Woeser
# Credit: 
# Description: Introduction to programming problem set uses Python
# numeric data types and operations to solve a variety of small problems. 

#
# Question 1
#

print("Question 1")
print("------------------------------------------")

# Calculate the number of watermelons given 70 children at 3 slices,
# 80 adults at 2 slices, 14 slices per watermelon, add 25% extra, rounding up.


import math
# Initialize variables with values
# ** your code **
children = 70
slices_per_adult = 2
slices_per_watermelon = 14
slices_per_child = 3
adults = 80
extra = 0.25


# Calculate total number of watermelon slices and display number of slices
# ** your code **
total_slices = (children * slices_per_child) + (adults * slices_per_adult)
print("Total slices:", total_slices)

# Add extra amount and display number of slices
# ** your code **
total_slices = total_slices + (total_slices * extra)
print("Total slices (including extra):", total_slices)

# Calculate number of watermelons and display number of watermelons
# ** your code **
watermelons = total_slices / slices_per_watermelon
print("Total watermelons", watermelons)

# Round the number of watermelons up and display number of watermelons
# ** your code **
watermelons = math.ceil(watermelons)
print("Total watermelons (rounded up)", (watermelons))




#
# Question 2
#
print()
print("Question 2")
print("------------------------------------------")

# Calculate total number of trips given 50, 100, 200 or 500 daily steps, 14
# steps per floor, and down and back up the stairs as one trip. Re-use the
# step variable. Round the number of trips up to the nearest whole integer.
# Recommended variable names: steps_per_floor, target_steps, trips

# Initialize variables
# ** your code **
floor = 0
steps_per_floor = 14 * 2
target_steps = 50, 100, 150, 500

# Calculate 50 steps and display number of trips
# ** your code **
fifty = target_steps[0] / steps_per_floor 
print("Trips for 50 steps:", math.floor(fifty))

# Calculate 100 steps and display number of trips
# ** your code **
hundred = target_steps[1] / steps_per_floor 
print("Trips for 100 steps:", math.floor(hundred))

# Calculate 200 steps and display number of trips
# ** your code **
one_fifty = target_steps[2]  / steps_per_floor 
print("Trips for 150 steps:", math.floor(one_fifty))

# Calculate 500 steps and display number of trips
# ** your code **
five_hun = target_steps[3] / steps_per_floor
print("Trips for 500 steps:", math.floor(five_hun))




#
# Question 3
#
print()
print("Question 3")
print("------------------------------------------")

# Calculate total distance walked per week given a pivot radius of 200 feet,
# six pivots, two inspections per day, and working five days a week. Round
# all results to two decimal places. Use 3.14, or math.pi, for the circumference
# equation calculation.

# Initialize variables
# ** your code **
pivot_radius = 200
number_of_pivots = 6
inspections_per_day = 2
days_worked = 5
number_of_inspections = inspections_per_day * days_worked

# Calculate circumference of one pivot
# ** your code **
circ = 2*math.pi*pivot_radius

# Calculate and display total distance walked (feet and miles)
# ** your code **
ft_distance = circ * number_of_pivots * number_of_inspections
miles_distance = ft_distance / 5280

print('Weekly distance (feet):', round(ft_distance, 2))
print('Weekly distance (miles):', round(miles_distance, 2)) 


