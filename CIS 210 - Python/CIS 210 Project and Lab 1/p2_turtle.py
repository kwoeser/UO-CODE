# CIS 210 Winter 2021 Project 1
# Karma Woeser
# Project 1 - Turtle Graphics

import turtle
t = turtle.Turtle()

# Background color, hides turtle and increates speed
turtle.Screen().bgcolor('skyblue')
t.hideturtle()
t.speed(15)

def water(t, x, y):
    '''Purpose: draws water

    Args: t is the turtle
    x and y are the position to where the turtle will go to
    
    Picks up turtle then goes to the x y cords. Then draws the water
    '''
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color('blue')

    t.begin_fill()
    for i in range(4):
        t.forward(780)
        t.right(90)
    t.end_fill()
    
water(t, -400, -100)


def body(t, x, y):
    '''Purpose: draws body of duck

    Args: t is the turtle
    x and y are the position to where the turtle will go to
    
    Goes to the x y cords and draws the body of the duck (oval)
    '''
    t.pu()
    t.goto(x, y)
    t.pd()

    t.right(45)
    t.color('yellow')
    t.begin_fill()
    for i in range(2):
        t.circle(180, 90)
        t.circle(90, 90)
    t.end_fill()
    
body(t, -75, -45)


def neck(t, x, y):
    '''Purpose: Draws the neck of duck

    Args: t is the turtle
    x and y are the position to where the turtle will go to
    
    Draws the neck by drawing a tiny square like shape
    '''
    t.pu()
    t.goto(x, y)
    t.pd()
    t.right(200)

    t.begin_fill()
    for i in range(4):
        t.right(90)
        t.forward(40)
    t.end_fill()

neck(t, -50, 140)


def head(t, x, y):
    '''Purpose: Draws the head of duck

    Args: t is the turtle
    x and y are the position to where the turtle will go to
    
    Goes to x y cords and drwas oval like head
    '''
    t.up()
    t.goto(x, y)
    t.pd()

    t.begin_fill()
    t.right(150)
    for i in range(2):
        t.circle(100, 90)
        t.circle(50, 90)
    t.end_fill()

head(t, -120, 150)


def eye(t, x, y, color):
    '''Purpose: Draws the eye

    Args: t is the turtle
    x and y are the position to where the turtle will go to
    color: color of the turtle
    
    Draws tiny eye on head by using circle
    '''
    t.color(color)
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
eye(t, -100, 200 , 'black')


def beak(t, x , y, color):
    '''Purpose: Draws the beak

    Args: t is the turtle
    x and y are the position to where the turtle will go to
    color: color of the turtle
    
    Drwas beak by drawing a tiny triangle like shape
    '''
    t.up()
    t.color(color)
    t.right(150)
    t.goto(x, y)
    t.pd()

    t.begin_fill()
    t.forward(45)
    t.right(150)
    t.forward(51)
    t.end_fill()


beak(t, -140, 180, 'orange')











