from random import randint
import time

def createNumber():
    number=randint(1,100)
    return number

def findNumber():
    myGuess=int(input("Aklinizdaki sayiyi giriniz : "))
    time.sleep(1)
    if(myGuess==createNumber()):
        print("sayiyi dogru tahmin ettiniz")
        return False
    print("tahmininiz yanlis")
    return True

loop = True
createNumber()
while(loop):
   loop=findNumber()
   exit = input("oyundan cikmak icin q ya basiniz : ")
   if(exit=='q'):
       loop=False    