# CIS 122 Fall 2020 Lab 2 Cement
# Author: Karma Woeser
# Partner: Your Partner
# References: https://www.calculatorsoup.com/calculators/math/speed-distance-time-calculator.php
# Description: Travel Time problem

def calc_travel_time(distance, speed):
    # Divides distnace by speed and multipies that result by 60
    time = (distance/speed) * 60

    # Rounds time to the second decimal point and returns 
    return round(time, 2)


def print_travel_time(distance, speed):
    # Hours and Mins are set as integers.
    hours = int(distance/speed)
    # Divides distance by speed and multiplies that by 60. The result of that is divided by 60 and the reminder of the result is set as minutes.
    mins = int((distance/speed)*60%60)
    # Same thing as minutes but times it by 3600 instead of 60.
    secs = round((distance/speed)*3600%60)

    # String concatnation
    string = 'To travel ' + str(distance) + ' miles at ' + str(speed)
    string_two= ' MPH it will take ' + str(hours) + ' hours, ' + str(mins)
    string_three = ' minutes, ' + str(secs) + ' sec.'
    
    print(string + string_two + string_three)

# Calls the print_travel_time function and sets two paramters 
print_travel_time(90, 55)
print_travel_time(90, 70)
print_travel_time(10, 25)
print_travel_time(10, 35)
