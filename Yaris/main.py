from turtle import Turtle,Screen
import random


screen=Screen()
screen.setup(width=500,height=400)


myTurtle=Turtle()
myTurtle.shape("turtle")
myTurtle.penup()
myTurtle.goto(-230,0)

allTurtle=[]
cordiniant=[-50,-25,25,50]
color=["red","blue","orange","green"]
ilerlemeListesi=[4,5,6,7,8,9,10,11,12,13]

for turtleIndex in range(0,4):
    newTurtle=Turtle("turtle")
    newTurtle.penup()
    newTurtle.color(color[turtleIndex])
    newTurtle.goto(-230,cordiniant[turtleIndex])
    allTurtle.append(newTurtle)

inRace=True
allTurtle.append(myTurtle)

while(inRace):

    for turtleIndex in allTurtle:
        if turtleIndex.xcor()>200:
            print(turtleIndex.color())
            inRace=False
            break
        turtleIndex.forward(random.choice(ilerlemeListesi))




screen.exitonclick()
