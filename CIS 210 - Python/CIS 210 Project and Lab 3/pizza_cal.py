# CIS 210 Winter 2021-2022 Lab 3
# Karma Woeser
# Lab 3 - Pizza Cal

# Pizza calculator example code  
import math

def pizza_CPSI(diameter, cost):  
    '''  
    (int, num) -> float  
 
    Calculates and returns the cost per square inch  
    of pizza for a pizza of given diameter and cost.  
    Examples:  
 
    >>> pizza_CPSI(14, 18)  
    0.117 
    >>> pizza_CPSI(14, 20.25)   
    0.132 
    '''  
 
    #r = diameter / 2  
    #area = math.pi * r**2
    area = circle_area(diameter)
 
    cost_per_inch = cost / area  
    cost_per_inch = round(cost_per_inch, 3)  
    return cost_per_inch, area




def circle_area(diameter: float) -> float:
    '''
    Returns the area of a circle

    Args:
    (float) diameter

    Returns:
    area: (float) area of the circle

    >>> circle_area(0)
    0.0
    >>> circle_area(20)
    314.1592653589793
    '''
    radius = diameter / 2
    area = math.pi * radius * radius

    return area


diameter = 20  
cost = 31.42  
#pizza_CPSI(diameter, cost)
cpi, area = pizza_CPSI(diameter, cost)




