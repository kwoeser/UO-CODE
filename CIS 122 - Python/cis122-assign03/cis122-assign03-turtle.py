# CIS 122 Fall 2020 Lab 3 Turtle
# Author: Karma Woeser
# Partner: Your Partner
# References: 
# Description:Turtle problem

import turtle
t = turtle.Turtle()

def draw_line(t, x, y, angle, length):
    """Purpose: To draw a line.
    This function draws a line by setting a x and y position, an angle, and
    a length of the line. All this will be calcuated into a line.

    Args: t is the turtle
    x and y are the (x,y) position that the turtle will be at when starts to draw the line
    angle is the angle where the turtle will draw in
    length is how long the line will be

    Returns: None
    Question for the person grading - I'm not sure wheter to put None or draws a line.
    Since it's turtle it doesn't actually print or return anything so I'm just put None. I hope
    that's fine.
    """
    t.pu()
    t.setx(x)
    t.sety(y)
    t.seth(angle)
    t.pd()
    t.fd(length)
    
#draw_line(t, 50, 50, 0 ,50)
#draw_line(t, -50, -50, 135, 75)
#draw_line(t, 100, -100, 275, 100)



def draw_radial_lines(t, x, y, length, num_lines):
    """Purpose: Draw radial lines
    This function has a for loop that will draw lines depending on the argument that is
    given by the draw_radials_in_quadrants function. Radials are a circle shape so a 360
    degree of lines needs to be drawn. The draw_line function is called which draws each
    line.
    
    Args: t is the turtle
    x and y are the (x,y) position that the turtle will be at when starts to draw the line
    length is how long the line will be
    num_lines are the number of lines that will be drawn

    Returns: None
    Question for the person grading - I'm not sure wheter to put None or draws a line.
    Since it's turtle it doesn't actually print or return anything so I'm just put None. I hope
    that's fine.
    """
    
    angle = 0
    for i in range(num_lines):
        angle += 360/num_lines
        draw_line(t, x, y, angle, length)

#draw_radial_lines(t, -50, -50, 10 ,4)
#draw_radial_lines(t, -50, 50, 20 ,8)
#draw_radial_lines(t, 50, -50, 40 ,16)
#draw_radial_lines(t, 50, 50, 80 ,20)



def draw_radials_in_quadrants(t, length, num_lines):
    """Purpose: Draw radials in different quadrants 
    This function draws radials in four quadrants. The quadrant that the lines are drawn
    in is based off the x and y cords that are given. This function calls the draw_radial_lines
    function.

    Args: t is the turtle
    length is how long the line will be
    num_lines are the number of lines that will be drawn

    Returns: None, not sure once again but on the assignment it said it's a void function.
    Sorry if this is unnessicary
    Four radials in four different quadrants.
    """
    # Top right
    draw_radial_lines(t, 125, 125, length, num_lines)
    # Top left
    draw_radial_lines(t, -125, 125, length, num_lines)
    # Bottom left
    draw_radial_lines(t,-125, -125, length, num_lines)
    # Bottom Right
    draw_radial_lines(t, 125, -125, length, num_lines)

    
draw_radials_in_quadrants(t, 75, 16)
#draw_radials_in_quadrants(t, 25, 3)
#draw_radials_in_quadrants(t, 50, 9)
