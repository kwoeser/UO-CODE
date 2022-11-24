# CIS 210 Winter 2021-2022 Project 3
# Karma Woeser
# Project 3 - Archimedes Method 

import math

def pi_arch(num_sides: int) -> float:
    '''
    Explaination: Function uses the Archimedes method to approximate the value of pi

    Parameters: num_sides: the number of sides

    Returns: pi

    >>> pi_arch(100)
    3.141075907812829

    >>> pi_arch(0.5)
    -1.2246467991473532e-16
    '''
    
    innerAngleB = 360.0 / num_sides
    halfAngleA = innerAngleB / 2
    
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    
    polygonCircumference = num_sides *  sideS
    pi = polygonCircumference / 2
    return pi



