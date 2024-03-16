
from turtle import Turtle,Screen

eray=Turtle()
eray.shape("turtle")
eray.color("blue")
eray.speed(1)
for x in range(0,18):
    liste=[120,90,72,60]
    eray.forward(100)
    if(x<3):
        eray.right(liste[0])
    elif(x<7 and x>=3):
        eray.color("red")
        eray.right(liste[1])
    elif(x>=7 and x<12):
        eray.color("orange")
        eray.right(liste[2])
    else:
        eray.color("black")
        eray.right(liste[3])
screen=Screen()
screen.exitonclick()
