from Snake import snake
from turtle import Turtle
from random import randint

class food:
    snake=snake()
    myDot = Turtle()
    def __init__(self):

        self.myDot.shape("circle")
        self.myDot.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.myDot.color("blue")
        self.myDot.penup()
        self.randomCordiant()


    def randomCordiant(self):
        corX=(10*randint(-27,27))
        corY=(10*randint(-27,27))
        self.myDot.goto(corX,corY)

    def yedimi(self):
        if(self.snake.turtlePool[0].distance(self.myDot.xcor(),self.myDot.ycor())<12):
            self.randomCordiant()
            return True
        return False