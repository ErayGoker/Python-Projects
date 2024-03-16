import turtle
from turtle import Screen,Turtle
import pandas
from tkinter import *
from tkinter import messagebox

true=0
screen=Screen()
screen.title("State Game")
image="blank_states_img.gif"
screen.setup(800,600)
screen.addshape(image)
screen.bgcolor("Grey")
turtle.shape(image)
turtle=Turtle()

turtle.penup()


data=pandas.read_csv("50_states.csv")
hataHakki=3
correctState=[]
def kontrol(answer):
    dataStates=data.state.to_list()
    global hataHakki
    root = Tk()
    if answer in correctState:
        messagebox.showinfo("showinfo", f"bu eyaleti isaretli {answer}")
        root.destroy()
        return False
    if not answer in dataStates:
        hataHakki -= 1
        messagebox.showerror("Show Error", f"hata hakkiniz {hataHakki} kaldi")
        root.destroy()
        return False
    root.destroy()
    return True

while true<50 and hataHakki!=0:
    title = f"{true}/50 state correct"
    answer = screen.textinput(title, "Sehir ismi giriniz")
    if kontrol(answer):
        correctState.append(answer)
        dataState = data[data["state"] == answer]
        turtle.goto(int(dataState["x"]),int(dataState["y"]))
        turtle.write(answer)
        true+=1




screen.mainloop()

