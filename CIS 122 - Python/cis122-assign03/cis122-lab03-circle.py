# CIS 122 Fall 2020 Lab 3 Circle
# Author: Karma Woeser
# Partner: Your Partner
# References: 
# Description: Circle problem

# Import Turtle graphics module and create a turtle for drawing
import turtle
t = turtle.Turtle()


def move(t, x, y):
   # Picks up the and uses the goto method to make the turtle move to the x,y
   t.pu()
   t.goto(x, y)
   #Puts the pen back down to draw 
   t.pd()

   
def draw_circle(t, radius, x, y):
   # Calls the move function
   move(t, x, y - radius)
   # Draws a circle when given an radius
   t.circle(radius)

draw_circle(t, 50, 0, 0)
draw_circle(t, 75, 0, 0)
draw_circle(t, 100, 0, 0)


def draw_concentric_circles(t, amount, start_size, radius, x, y):
   # Loops for the amount of circles I want to create; so 3 times
    for i in range(amount):
       # Calls the draw_cricle function
       draw_circle(t, start_size, 0, 0)
       # Adds radius to start_size and makes the result of that the new start_size
       start_size += radius

# Changed the start_size to 125 so it expands the circle that was already made 
draw_concentric_circles(t, 3, 125, 25, 0, 0)
