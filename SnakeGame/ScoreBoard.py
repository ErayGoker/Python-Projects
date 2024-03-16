from turtle import Turtle
from SnakeFood import food
class board(food):

    def __init__(self):
        super().__init__()
        self.score=0
        self.myScore=Turtle()
        self.myScore.color("pink")
        self.myScore.penup()
        self.myScore.goto(0, 280)
        self.updateWrite()


        self.myScore.hideturtle()

    def updateWrite(self):
        self.myScore.write(f"Score : {self.score} ", align="center", font=("arial", 12, "normal"))


    def Score(self):
        self.score+=1
        self.myScore.clear()
        self.updateWrite()