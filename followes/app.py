from data import Data
import random


def dataAta():
    return random.choice(Data)

def kontrol(birinci,ikinci,tahmin):
    cevap=0
    if(birinci["follower_count"]<ikinci["follower_count"]):
        cevap=2

    else:
        cevap=1


    if(tahmin==cevap):
        return True
    return False

def game():
    kontrolEt=True
    dogruCevap=0
    birinci=dataAta()
    ikinci=dataAta()

    while(kontrolEt):
        print(birinci["description"]+" "+birinci[ "name"])
        print(ikinci["description"]+" "+ikinci["name"])
        myAnswer=int(input("hangisinin fazla takipcisi oldugunu giriniz "))
        kontrolEt=kontrol(birinci,ikinci,myAnswer)
        if(kontrolEt==True):
            dogruCevap+=1
            print("cevabiniz dogru ")
            if(myAnswer==1):
                ikinci=dataAta()
            else:
                birinci=dataAta()
        else:
            print(f"cevap yanlis puaniniz { dogruCevap}")


game()