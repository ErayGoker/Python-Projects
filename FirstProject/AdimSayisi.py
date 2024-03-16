from random import randint
import threading 
import time

list=[]
count=0

def write():
    global count
    global list
    
    randomNumber=randint(0,1)
    list.append(randomNumber)
    
    if(list[0]==1):
        count+=1
    
    x=0
    while(True):
        time.sleep(0.2)
        randomNumber=randint(0,1)
        list.append(randomNumber)
        if( x!=0 and list[x+1]==0 and (list[x]!=list[x+1])):
            count+=1
        x+=1
        

def read():
    global list
    global count
    while(True):
        print(list)
        print("loop : ",count,"\n")
        time.sleep(0.5)
    

thrdWrite=threading.Thread(target=write)
thrdRead=threading.Thread(target=read)

thrdWrite.start()
thrdRead.start()

thrdWrite.join()
thrdRead.join()
    
