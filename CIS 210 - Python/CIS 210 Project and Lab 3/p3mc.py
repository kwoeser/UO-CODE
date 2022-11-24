# CIS 210 Winter 2021-2022 Project 3
# Karma Woeser
# Project 3 - Monte Carlo Simulation

import math
import random

def pi_mc(num_darts: int) -> float:
    '''
    Explaination: Finds the approxamation of pi using the Monte Carlo method

    Parameters: num_darts: number of darts thrown

    Returns: pi

    >>> pi_mc(100)
    3.12

    >>> pi_mc(5)
    3.2
    '''
    random.seed(10)
    inCircle = 0
    
    for i in range(num_darts):
        x = random.random()
        y = random.random()
        distance = math.sqrt(x**2  +  y**2)    #compute distance from (0, 0)
        
        if distance <= 1:
            inCircle = inCircle + 1
            
    pi = inCircle / num_darts * 4
    return pi

print(pi_mc(0))
