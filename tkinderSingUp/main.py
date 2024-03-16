import tkinter.messagebox
from tkinter import *

def addLogin(e=None):
    kontrol=True
    with open("hesaplar.txt","r+") as file:
        hesaplar=file.readlines()
        if len(hesaplar)==0:

            file.write(entryWebSites.get() + " | " + entryEmail.get() + " | " + entryPassword.get() + "\n")
        else:
            for x in hesaplar:
                if (entryWebSites.get() or entryEmail.get() and entryPassword.get()) in x:
                    kontrol=False
                    break
            if kontrol==False:
                tkinter.messagebox.showerror(message="bu hesap txt dosyasinda zaten mevcut lutfen kontrol ediniz")
            else:
                file.write(entryWebSites.get() + " | " + entryEmail.get() + " | " + entryPassword.get()+ "\n")
                entryPassword.delete(0,END)
                entryWebSites.delete(0,END)


def createPassword(e=None):
    entryPassword.insert(0,"eray <3 yasmin ")

window=Tk()
window.title("create password")
window.configure(background="black")
window.geometry("420x360")
canvas=Canvas(width=180,height=180)
window.config(padx=5,pady=10)
logoImg=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logoImg)
canvas.place(x=110,y=1)
canvas.configure(background="black",highlightthickness=0)

labelWebSite=Label(text="Web sitesi : ",background="black",highlightthickness=0,fg="white")
labelWebSite.place(x=10,y=200,)

entryWebSites=Entry(width=30)
entryWebSites.place(x=140,y=200,)


labelEmail=Label(text="Email/Username : ",background="black",highlightthickness=0,fg="white")
labelEmail.place(x=10,y=240)

entryEmail=Entry(width=30)
entryEmail.place(x=140,y=240)

labelPassword=Label(text="Password : ",background="black",highlightthickness=0,fg="white")
labelPassword.place(x=10,y=280)

entryPassword=Entry(width=17)
entryPassword.place(x=140,y=280)


button=Button(text="sifre olustur",width=12 ,padx=0,pady=1,background="black",highlightthickness=0,fg="white",command=createPassword)
button.place(x=284,y=280)

add=Button(text="add",width=30,padx=0,pady=0,background="black",highlightthickness=0,fg="white",command=addLogin)
add.place(x=140,y=310)


entryPassword.bind("<Return>",addLogin)


window.mainloop()