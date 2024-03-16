from turtle import Turtle,Screen

myTurtle=Turtle()

def ileri():

    myTurtle.forward(10)

def geri():

    myTurtle.backward(10)


def solaDon():
    heading=myTurtle.heading()+10
    myTurtle.setheading(heading)

def sagaDon():
    heading=myTurtle.heading()-10
    myTurtle.setheading(heading)


screen=Screen()
screen.listen()
screen.onkey(ileri,"w")
screen.onkey(geri,"s")
screen.onkey(solaDon,"a")
screen.onkey(sagaDon,"d")


screen.exitonclick()