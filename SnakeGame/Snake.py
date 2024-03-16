from turtle import Screen,Turtle
import time

class snake():
    turtlePool = []
    def __init__(self):
        myTurtle = Turtle()
        myTurtle.color("white")
        myTurtle.penup()
        myTurtle.shapesize(0.5)
        myTurtle.shape("square")


        self.turtlePool.append(myTurtle)
        self.creatTurtle()
        self.creatTurtle()

    def creatTurtle(self):
        newTurtle = Turtle()
        newTurtle.color("white")
        newTurtle.penup()
        newTurtle.shapesize(0.5)
        newTurtle.shape("square")
        self.turtlePool.append(newTurtle)
        newTurtle.goto(-((len(self.turtlePool) - 1) * 10), 0)

    def move(self):
        for x in range(len(self.turtlePool) - 1, 0, -1):
            cordionatX = self.turtlePool[x - 1].xcor()
            cordionatY = self.turtlePool[x - 1].ycor()
            self.turtlePool[x].goto(cordionatX, cordionatY)



        if(int(self.turtlePool[0].xcor())>=285):
            ycor=self.turtlePool[0].ycor()
            self.turtlePool[0].goto(-280,ycor)

        elif int(self.turtlePool[0].ycor())>=285:
            xcor = self.turtlePool[0].xcor()
            self.turtlePool[0].goto(xcor,-280)

        elif int(self.turtlePool[0].ycor()) <= -285:
            xcor = self.turtlePool[0].xcor()
            self.turtlePool[0].goto(xcor,280)

        elif (int(self.turtlePool[0].xcor()) <= -285):
            ycor = self.turtlePool[0].ycor()
            self.turtlePool[0].goto(280, ycor)

        self.turtlePool[0].forward(10)


    def sagaDon(self):
        if (self.turtlePool[0].heading() != 90):
            self.turtlePool[0].setheading(270)

    def solaDon(self):
        if (self.turtlePool[0].heading() != 270):
            self.turtlePool[0].setheading(90)

    def duzGit(self):
        if (self.turtlePool[0].heading() != 180):
            self.turtlePool[0].setheading(0)

    def arkaya(self):
        if (self.turtlePool[0].heading() != 0):
            self.turtlePool[0].setheading(180)

    def showCordiniantX(self):
        return self.turtlePool[0].xcor()

    def showCordiniantY(self):
        return self.turtlePool[0].ycor()

    def bittiMi(self):
        for x in self.turtlePool:
            if(x==self.turtlePool[0]):
                continue
            elif(self.turtlePool[0].xcor()==x.xcor()and self.turtlePool[0].ycor()==x.ycor()):
                return False

        return True

