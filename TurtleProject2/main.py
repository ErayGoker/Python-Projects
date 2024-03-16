import random
import turtle
from turtle import Turtle,Screen

myTurtle=Turtle()
myTurtle.shape("turtle")
turtle.colormode(255)

acilar=[0,90,180,270]
def setColor():
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    randomColor=(r,b,g)
    return randomColor


turtle.speed("fastest")
size=1
while(True):
    myTurtle.forward(30)
    myTurtle.right(random.choice(acilar))
    myTurtle.color(setColor())
    myTurtle.pensize(size)
    size+=0.01




screen=Screen()
screen.exitonclick()