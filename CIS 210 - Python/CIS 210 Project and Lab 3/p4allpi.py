# CIS 210 Winter 2021-2022 Project 3
# Karma Woeser
# Project 3 - p4allpi

import math
import random
from p1arch import *
from p2wallis import * 
from p3mc import *


def pi_allpi(err_tol: float):
    '''
    Explaination:
    Finds the requirements to find the approximation of pi using error tolerence

    Parameters:
    err_tol (float): the error tolerence and is between 0 and 1

    Returns:
    The requiremnts that are needed to solve for the approximation of pi

    >>> pi_allpi(0.1)
    Archimedes: num_sides =  8
    Wallis: num_pairs =  8
    Monte Carlo: num_darts =  5
    [8, 8, 5]

    >>> pi_allpi(0.001)
    Archimedes: num_sides =  72
    Wallis: num_pairs =  785
    Monte Carlo: num_darts =  177
    [72, 785, 177]
    '''
    random.seed(42)
 
    # Archimedes Method
    num_sides = 0
    while True:
        num_sides += 1
        # Finds value between math.pi - err_tol and math.pi + err_tol
        if ((math.pi - err_tol) <= pi_arch(num_sides) <= (math.pi + err_tol)):
            print("Archimedes: num_sides = ", num_sides)
            break
            
    # Wallis Method
    num_pairs = 0
    while True:
        num_pairs += 1
        if ((math.pi - err_tol) <= pi_wallis(num_pairs) <= (math.pi + err_tol)):
            print("Wallis: num_pairs = ", num_pairs)
            break


    # Monte Carlo Method
    num_darts = 0
    while True:
        num_darts += 1
        if ((math.pi - err_tol) <= pi_mc(num_darts) <= (math.pi + err_tol)):
            print("Monte Carlo: num_darts = ", num_darts)
            break


    pi_list = [num_sides, num_pairs, num_darts]
    print(pi_list)






