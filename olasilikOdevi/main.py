import math
import tkinter.messagebox
from tkinter import *
import random
import pandas
from collections import Counter
window=Tk()

def removeWidget():
    for widget in window.winfo_children():
        widget.destroy()
def basicRandomNumber():
    removeWidget()
    def createRandomNubmer(e=None):
        numbers=[]

        if(maxInput.get()=="" or minInput.get()=="" or nInput.get()==""):
            tkinter.messagebox.showerror(title="error message",
                        message="tum bilgileri girdiginizden emin olunuz")

        if(int(maxInput.get())<int(minInput.get())):
            tkinter.messagebox.showerror(title="error message",message="maxsimin sayiniz minimum sayinizdan buyuk olmak zorundadir")

        while(len(numbers)<int(nInput.get())):
            if(int(maxInput.get())-int(minInput.get())>=int(nInput.get())):
                randomNumber=random.randint(int(minInput.get()),int(maxInput.get()))
                if not randomNumber in numbers:
                    numbers.append(randomNumber)
            elif(int(maxInput.get())-int(minInput.get())<=int(nInput.get())):
                numbers.append(random.randint(int(minInput.get()),int(maxInput.get())))


        tkinter.messagebox.showinfo(title="product numbers",message=str(numbers))

    window.title("basicRandomNumber")
    window.minsize(300, 300)
    window.configure(bg="black")

    minLabel = Label(text="minimum sayiyi giriniz :",fg="white" ,bg="black")
    minLabel.place(x=10, y=100)

    minInput = Entry(width=6)
    minInput.place(x=200, y=100)

    geri = Button(text="<--", fg="white", bg="black", highlightthickness=0, command=main)
    geri.place(x=10, y=10)

    maxLabel = Label(text="maxsimum sayiyi giriniz :" ,fg="white" ,bg="black")
    maxLabel.place(x=10, y=150)
    maxInput = Entry(width=6)
    maxInput.place(x=200, y=150)

    nLabel = Label(text="kac tane deger uretilecek:" ,fg="white" ,bg="black")
    nLabel.place(x=10, y=200)
    nInput = Entry(window, width=6)
    nInput.place(x=200, y=200)

    hesapla = Button(text="hesapla", command=createRandomNubmer ,fg="white" ,bg="black")
    hesapla.place(x=190, y=250)

    nInput.bind('<Return>', createRandomNubmer)
    hesapla.bind('<Return>', createRandomNubmer)
    maxInput.bind('<Return>', createRandomNubmer)
    minInput.bind('<Return>', createRandomNubmer)

def systematicNumber():
    removeWidget()
    def createNumber(e=None):

        if (maxInput.get() == "" or nInput.get() == ""):
            tkinter.messagebox.showerror(title="error message",
                                         message="tum bilgileri girdiginizden emin olunuz")

        k=int(int(maxInput.get())/int(nInput.get()))
        a=random.randint(1,k)
        numbers=[a]
        for x in range(1,int(nInput.get())):
            numbers.append(a+(x*k))

        tkinter.messagebox.showinfo(title="Producter numbers",message=str(numbers))


    window.wm_minsize(300,300)
    window.configure(background="black")
    window.title("systematicNumber")

    maxLabel=Label(text="Evrenin boyutunu giriniz :" ,bg="black",fg="white")
    maxLabel.place(x=10,y=100)
    maxInput=Entry(width=6)
    maxInput.place(x=210,y=100)

    geri = Button(text="<--", fg="white", bg="black", highlightthickness=0, command=main)
    geri.place(x=10, y=10)

    nLabel = Label(text="Kac tane deger uretilecek:", fg="white", bg="black")
    nLabel.place(x=10, y=150)
    nInput = Entry(window, width=6)
    nInput.place(x=210, y=150)

    hesapla = Button(text="Hesapla",command=createNumber, fg="white", bg="black")
    hesapla.place(x=200, y=200)

    nInput.bind('<Return>', createNumber)
    hesapla.bind('<Return>', createNumber)
    maxInput.bind('<Return>', createNumber)


def floatVeriler():

    removeWidget()
    datas =[]




    def verTemizle(e=None):
        datas.clear()

    def veriEkle(e=None):
        if(inputData.get()!=""):
            datas.append(float(inputData.get()))
            inputData.delete(0,"end")

        return datas



    def basitSeri():
        string=""
        newList=sorted(datas)

        for x in newList:
            string+=str(x)
            string+=","
        tkinter.messagebox.showinfo(title="basit Seri",message=string)


    def frekansSeri():
        direct=[]
        liste=[]
        endList = []
        sortList=sorted(datas)
        for x in sortList:
            count=0
            if not x in liste:
                for y in sortList:
                    if x==y:
                        count+=1
                direct.append([x,count])
                liste.append(x)
            else:
                continue

        for x in range(0,len(direct)):
            endList.append({"veri" :direct[x][0],"frekans":direct[x][1]})

        dataFrameList=pandas.DataFrame(endList)
        tkinter.messagebox.showinfo(title="frekans serisi",message=str(dataFrameList))

        direct.clear()
        liste.clear()


    def tablo():
        N=int(len(datas))
        if math.sqrt(len(datas)) > int(math.sqrt(len(datas))):
            K=int(math.sqrt(len(datas))+1)
        else:
            K=int(math.sqrt(len(datas)))

        R=float(float(max(datas)) - float(min(datas)))

        if R/K > int(R/K):
            H=int(R/K)+1
        else:
            H = int(R / K)

        minDeger=[round(float(min(datas)),2)]
        for x in range(int(K-1)):
            minDeger.append(round(minDeger[0]+((H*(x+1))),2))


        directory=[{"sinir alt limiti":minDeger}]

        maxDeger=[]
        for x in range(int(K-1)):
            maxDeger.append(round(float(minDeger[x+1]-0.1),2))

        maxDeger.append(round(maxDeger[K-2]+H,2))
        directory.append({"sinir ust limitleri":maxDeger})

        sinifMinDeger=[round(float(min(minDeger)-((minDeger[1]-maxDeger[0])/2)),2)]
        sinifMaxDeger=[round(float(min(maxDeger)+((minDeger[1]-maxDeger[0])/2)),2)]



        for x in range(int(K)-1):
            sinifMinDeger.append(round(float(sinifMinDeger[0]+((x+1)*H)),2))
            sinifMaxDeger.append(round(float(sinifMaxDeger[0]+((x+1)*H)),2))



        directory.append({"sinif alt sinirlari":sinifMinDeger})
        directory.append({"sinif ust sinirlari":sinifMaxDeger})



        frekans=[]
        count = 0
        frekan = 0
        shortDatas=sorted(datas)
        for x in shortDatas:

            if x>=minDeger[count] and x<=maxDeger[count]:
                frekan+=1

            if x>maxDeger[count]:
                print(x)
                frekans.append(frekan)
                frekan=1
                count+=1

        frekans.append(frekan)


        directory.append({"sinif frekanslari":frekans})

        SON=[]
        for x in range(K):
            SON.append((maxDeger[x]+minDeger[x])/2)

        directory.append({"SON":SON})


        EF=[]
        efCount=0
        for x in frekans:
            if efCount==0:
                EF.append(frekans[efCount])

            else:
                EF.append(EF[efCount-1]+x)

            efCount+=1

        directory.append({"E.F":EF})

        OF=[]
        for x in frekans:
            OF.append(f"{x}/{N}")

        directory.append({"O.F":OF})

        EOF = []
        for x in EF:
            EOF.append(f"{x}/{N}")

        directory.append({"E.O.F": EOF})

        print(directory)


    def aritmetikModMedyanFonk():
        sum=0
        for x in datas:
            sum+=x
        ort=float(sum/len(datas))

        mod=0
        tekrarlar={}
        for x in datas:
            if x in tekrarlar:
                tekrarlar[x]+=1
            else:
                tekrarlar[x]=1
        for x,y in tekrarlar.items():
            enBuyuk=max(tekrarlar.values())
            if y==enBuyuk:
                mod=x


        sortList=sorted(datas)
        if len(datas)%2==0:
            ortaDeger=int(len(datas)/2)

            sum=float(sortList[ortaDeger]+sortList[ortaDeger-1])
            medyan=float(sum/2)
        else:
            ortaDeger=int((len(datas)+1)/2)
            medyan=float(sortList[ortaDeger-1])

        tkinter.messagebox.showinfo(message=f"""
aritmetik ortalama : {ort}
mod :{mod}
meydan : {medyan} 
        """)
        return ort

    def hoGo():
        carpim=1
        for x in datas:
            carpim*=x
        carpim=float(carpim**(1/len(datas)))

        sum=0
        for x in datas:
            sum+=x
        gO=float(len(datas)/(1/sum))

        tkinter.messagebox.showinfo(message=f"""
geometrik ortalama : {carpim}
hastonomik ortalama : {gO}
        
        """)


    def orneklemSapmaOms():
        ort = aritmetikModMedyanFonk()
        sum=0
        sum2=0
        for x in datas:
            sum+=(float((x-ort))**2)
            sum2+=abs(x-ort)


        orneklemVaryansi=float(sum/(len(datas)-1))

        standarSapma=float(math.sqrt(orneklemVaryansi))

        oms=float(sum2/len(datas))

        tkinter.messagebox.showinfo(message=f"""
orneklem varyansi : {orneklemVaryansi}
standart sapma : {standarSapma}
OMS : {oms}""")
        return standarSapma

    def carbasdeg():
        sapma = orneklemSapmaOms()
        sum = 0
        for x in datas:
            sum += x
        ort = sum / len(datas)

        sum2 = 0
        sum3 = 0
        for x in datas:
            sum2 += (x - ort) ** 3
            sum3 += (x - ort) ** 4

        carpiklik = sum2 / (len(datas) - 1)
        baskililik = sum3 / (len(datas) - 1)
        degisimKatsayisi = sapma / ort

        tkinter.messagebox.showinfo(message=f"""baskililik : {baskililik}
carpiklik : {carpiklik}
degisim katsayi : {degisimKatsayisi}""")

    window.minsize(350,350)
    labelData=Label(text="verileri giriniz :",bg="black",fg="white")
    labelData.place(x=30,y=70)
    inputData=Entry(width=6)
    inputData.place(x=150,y=70)

    addButton=Button(text="ekle",fg="white",bg="black",command=veriEkle)
    addButton.place(x=230,y=50)

    temizle = Button(text="verileri sil", fg="white", bg="black", command=verTemizle)
    temizle.place(x=220, y=90)

    geri = Button(text="<--", fg="white", bg="black",highlightthickness=0,command=main)
    geri.place(x=10, y=10)

    basitSeriButton = Button(text="basit seri", fg="white", bg="black", command=basitSeri)
    basitSeriButton.place(x=10, y=180)

    frekansSeriButton = Button(text="frekans seri", fg="white", bg="black", command=frekansSeri)
    frekansSeriButton.place(x=120, y=180)

    tabloButton = Button(text="tablo", fg="white", bg="black", command=tablo)
    tabloButton.place(x=250, y=180)


    hoGo = Button(text="H.O - G.O", command=hoGo,fg="white",bg="black")
    hoGo.place(x=220, y=230)

    varyansSapmaOms = Button(
text="""aritmetik,mod,medyan
varyans,sapma,OMS
baskililik,carpiklik,degisim""", command=carbasdeg,fg="white",bg="black")
    varyansSapmaOms.place(x=10, y=230)

    inputData.bind('<Return>', veriEkle)


def intVeriler():
    removeWidget()
    datas = []

    def verTemizle(e=None):
        datas.clear()

    def veriEkle(e=None):
        if (inputData.get() != ""):
            datas.append(int(inputData.get()))
            inputData.delete(0, "end")

        return datas

    def basitSeri():
        string = ""
        newList = sorted(datas)

        for x in newList:
            string += str(x)
            string += ","
        tkinter.messagebox.showinfo(title="basit Seri", message=string)

    def frekansSeri():
        direct = []
        liste = []
        endList = []
        sortList = sorted(datas)
        for x in sortList:
            count = 0
            if not x in liste:
                for y in sortList:
                    if x == y:
                        count += 1
                direct.append([x, count])
                liste.append(x)
            else:
                continue

        for x in range(0, len(direct)):
            endList.append({"veri": direct[x][0], "frekans": direct[x][1]})

        dataFrameList = pandas.DataFrame(endList)
        tkinter.messagebox.showinfo(title="frekans serisi", message=str(dataFrameList))

        direct.clear()
        liste.clear()

    def tablo():
        N = int(len(datas))
        if math.sqrt(len(datas)) > int(math.sqrt(len(datas))):
            K = int(math.sqrt(len(datas)) + 1)
        else:
            K = int(math.sqrt(len(datas)))

        R = int(int(max(datas)) - int(min(datas)))

        if R / K > int(R / K):
            H = int(R / K) + 1
        else:
            H = int(R / K)

        minDeger = [int(min(datas))]
        for x in range(int(K - 1)):
            minDeger.append((minDeger[0] + ((H * (x + 1)))))



        directory = [{"sinir alt limiti": minDeger}]

        maxDeger = []
        for x in range(int(K - 1)):
            maxDeger.append(int(minDeger[x + 1] - 1))

        maxDeger.append((maxDeger[K - 2] + H))
        directory.append({"sinir ust limitleri": maxDeger})

        sinifMinDeger = [float(min(minDeger) - ((minDeger[1] - maxDeger[0]) / 2))]
        sinifMaxDeger = [float(min(maxDeger) + ((minDeger[1] - maxDeger[0]) / 2))]

        print(minDeger)
        print(maxDeger)

        for x in range(int(K) - 1):
            sinifMinDeger.append(float(sinifMinDeger[0] + ((x + 1) * H)))
            sinifMaxDeger.append(float(sinifMaxDeger[0] + ((x + 1) * H)))

        directory.append({"sinif alt sinirlari": sinifMinDeger})
        directory.append({"sinif ust sinirlari": sinifMaxDeger})



        frekans = []
        count = 0
        frekan = 0
        shorDatas=sorted(datas)
        for x in shorDatas:

            if x >= minDeger[count] and x <= maxDeger[count]:
                frekan += 1

            if x > maxDeger[count]:
                print(x)
                frekans.append(frekan)
                frekan = 1
                count += 1

        frekans.append(frekan)

        directory.append({"sinif frekanslari": frekans})

        SON = []
        for x in range(K):
            SON.append((maxDeger[x] + minDeger[x]) / 2)

        directory.append({"SON": SON})

        EF = []
        efCount = 0
        for x in frekans:
            if efCount == 0:
                EF.append(frekans[efCount])

            else:
                EF.append(EF[efCount - 1] + x)

            efCount += 1

        directory.append({"E.F": EF})

        OF = []
        for x in frekans:
            OF.append(f"{x}/{N}")

        directory.append({"O.F": OF})

        EOF = []
        for x in EF:
            EOF.append(f"{x}/{N}")

        directory.append({"E.O.F": EOF})

        print(directory)

    def aritmetikModMedyanFonk():
        sum = 0
        for x in datas:
            sum += x
        ort = float(sum / len(datas))

        mod = 0
        tekrarlar = {}
        for x in datas:
            if x in tekrarlar:
                tekrarlar[x] += 1
            else:
                tekrarlar[x] = 1
        for x, y in tekrarlar.items():
            enBuyuk = max(tekrarlar.values())
            if y == enBuyuk:
                mod = x

        sortList=sorted(datas)
        if len(datas) % 2 == 0:
            ortaDeger = int(len(datas) / 2)

            sum = int(sortList[ortaDeger] + sortList[ortaDeger - 1])
            medyan = float(sum / 2)
        else:
            ortaDeger = int((len(datas) + 1) / 2)
            medyan = int(sortList[ortaDeger - 1])

        tkinter.messagebox.showinfo(message=f"""
    aritmetik ortalama : {ort}
    mod :{mod}
    meydan : {medyan} 
            """)
        return ort

    def hoGo():
        carpim = 1
        for x in datas:
            carpim *= x
        carpim = float(carpim ** (1 / len(datas)))

        sum = 0
        for x in datas:
            sum += x
        gO = float(len(datas) / (1 / sum))

        tkinter.messagebox.showinfo(message=f"""
    geometrik ortalama : {carpim}
    hastonomik ortalama : {gO}

            """)

    def orneklemSapmaOms():
        ort = aritmetikModMedyanFonk()
        sum = 0
        sum2 = 0
        for x in datas:
            sum += (float((x - ort)) ** 2)
            sum2 += abs(x - ort)

        orneklemVaryansi = float(sum / (len(datas) - 1))

        standarSapma = float(math.sqrt(orneklemVaryansi))

        oms = float(sum2 / len(datas))

        tkinter.messagebox.showinfo(message=f"""
    orneklem varyansi : {orneklemVaryansi}
    standart sapma : {standarSapma}
    OMS : {oms}
        
    """)

        return standarSapma

    def carbasdeg():
        sapma=orneklemSapmaOms()
        sum=0
        for x in datas:
            sum+=x
        ort=sum/len(datas)

        sum2=0
        sum3=0
        for x in datas:
            sum2+=(x-ort)**3
            sum3+=(x-ort)**4

        carpiklik=sum2/(len(datas)-1)
        baskililik=sum3/(len(datas)-1)
        degisimKatsayisi=sapma/ort


        tkinter.messagebox.showinfo(
message=f"""baskililik : {baskililik}
carpiklik : {carpiklik}
degisim katsayi : {degisimKatsayisi}
""")



    window.minsize(350, 350)
    labelData = Label(text="verileri giriniz :", bg="black", fg="white")
    labelData.place(x=30, y=70)
    inputData = Entry(width=6)
    inputData.place(x=150, y=70)

    addButton = Button(text="ekle", fg="white", bg="black", command=veriEkle)
    addButton.place(x=230, y=50)

    temizle = Button(text="verileri sil", fg="white", bg="black", command=verTemizle)
    temizle.place(x=220, y=90)

    geri = Button(text="<--", fg="white", bg="black", highlightthickness=0, command=main)
    geri.place(x=10, y=10)

    basitSeriButton = Button(text="basit seri", fg="white", bg="black", command=basitSeri)
    basitSeriButton.place(x=10, y=180)

    frekansSeriButton = Button(text="frekans seri", fg="white", bg="black", command=frekansSeri)
    frekansSeriButton.place(x=120, y=180)

    tabloButton = Button(text="tablo", fg="white", bg="black", command=tablo)
    tabloButton.place(x=250, y=180)

    hoGo = Button(text="H.O - G.O", command=hoGo,fg="white",bg="black")
    hoGo.place(x=220, y=230)

    varyansSapmaOms = Button(
text="""aritmetik,mod,medyan
varyans,sapma,OMS
carpiklik,baskililik,degisim""", command=carbasdeg,fg="white",bg="black")
    varyansSapmaOms.place(x=10, y=220)

    inputData.bind('<Return>', veriEkle)
def main():
    removeWidget()
    window.title("Olasilik Odevi")
    window.configure(background="black")
    window.minsize(width=400,height=400)

    basicRandomNumberButton=Button(text="basicRandomNumber",command=basicRandomNumber,fg="white",bg="black")
    basicRandomNumberButton.place(x=50,y=200)

    systematicNumberButton=Button(text="systematicNumber",command=systematicNumber,fg="white",bg="black")
    systematicNumberButton.place(x=200,y=260)

    float = Button(text="float veriler", command=floatVeriler, fg="white", bg="black")
    float.place(x=50, y=280)

    int = Button(text="int veriler", command=intVeriler, fg="white", bg="black")
    int.place(x=200, y=330)
    window.mainloop()

main()