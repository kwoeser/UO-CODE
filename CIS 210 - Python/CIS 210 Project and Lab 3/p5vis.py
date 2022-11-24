# CIS 210 Winter 2021-2022 Project 3
# Karma Woeser
# Project 3 - p5vis

import math
import turtle
import random

def mc_vis(num_darts: int):
    '''
    Runs and graphs the Monte Carlo simulation

    Args:
    num_darts: The number of darts

    Returns:
    the approxmation of pi using the monte carlo method
    '''
    wn = turtle.Screen()
    t = turtle.Turtle()


    t.speed(10)

    wn.setworldcoordinates(-2, -2, 2, 2)

    t.up()
    t.goto(-1, 0)
    t.down()
    t.goto(1, 0)

    t.up()
    t.goto(0, 1)
    t.down()
    t.goto(0, -1)


    inCircle = 0
    t.up()
    for i in range(num_darts):
        x = random.random()
        y = random.random()
        distance = math.sqrt(x**2 +  y**2)


        # FIrst quadrant
        t.goto(x, y)
        
        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")

        else:
            t.color('red')
            
        t.dot()


         # Second Quadrant
        t.goto(-x, y)
        
        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")

        else:
            t.color('red')
            
        t.dot()


        # Third Quadrant
        t.goto(-x, -y)
        
        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")

        else:
            t.color('red')
            
        t.dot()

        
        # Fourth Quadrant
        t.goto(x, -y)
        
        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")

        else:
            t.color('red')
            
        t.dot()

       


    pi = inCircle / num_darts * 4
    wn.exitonclick()
    return pi


    
 

