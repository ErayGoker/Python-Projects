import random
import turtle
from turtle import Turtle,Screen

turtle.colormode(255)

def setColor():
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    color=(r,b,g)
    return color

myTurtle=Turtle()
myTurtle.speed(10)
for x in range(0,36):
    myTurtle.circle(100,360)
    myTurtle.setheading(x*10)
    myTurtle.color(setColor())



screen=Screen()
screen.exitonclick()