from turtle import Screen,Turtle
import time
from Snake import snake
from SnakeFood import food
from ScoreBoard import board


snake=snake()



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()

screen.onkey(snake.solaDon,"w")
screen.onkey(snake.sagaDon,"s")
screen.onkey(snake.duzGit,"d")
screen.onkey(snake.arkaya,"a")

screen.tracer(0)

food = food()
board=board()
screen.update()

oyun=True
while oyun:
    screen.update()
    time.sleep(0.03)

    if food.yedimi():
        snake.creatTurtle()
        board.Score()
    snake.move()
    oyun=snake.bittiMi()


screen.exitonclick()