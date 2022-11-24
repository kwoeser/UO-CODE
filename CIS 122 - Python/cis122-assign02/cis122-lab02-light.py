# CIS 122 Fall 2020 Lab 2 light
# Author: Karma Woeser
# Partner: Dis Teacher Wednesday 12 pm 
# Description: Light travels 


def avg_light_travel_seconds (distance_miles):
    # Divides distance by the speed of light (mps); then returns the result
    time = distance_miles / 186282
    return time


def print_results(planetary_object, time_to_object):
    # String concatnation
    string = "Light travels from the sun to " + planetary_object
    # Rounds time_to_object to the second decimal point and turns it into a string
    string_two = " at an average of " + str(round(time_to_object , 2)) + ' seconds. '
    
    print(string + string_two)


# Calls the print_results function and the two parameters
# The avg_light_travel_seconds function is called and a new parameter is set
# Leading time to equal new parameter divieded by the speed of light 
print_results('the Earth', avg_light_travel_seconds(93000000))
print_results('Jupiter', avg_light_travel_seconds(484000000))


