import math
import tkinter.messagebox
from tkinter import *
import random
import pandas
window=Tk()

def naiveBayesToplamOLasilik():
    removeWidget()
    window.title("basicRandomNumber")
    window.minsize(800, 600)
    window.configure(bg="white")
    global naiveBayes
    global toplamOlasilik
    def sorular():
        allQuestion=["Istenilen olay (E) olsun bu E olayina gore kosullarin olasiligini mi istiyorsunuz ","Sonuç olarak bir olayın genel olasılığını mı bulmak istiyorsunuz","bir olayın gerçekleşme olasılığını, bu olayın farklı olası koşullar altında hesaplayarak mi bulmak istiyorsunuz","Bir olayın gerçekleşme olasılığını, önceden bilinen bir testin sonucuna dayanarak mı hesaplamak istiyorsunuz?"]
        L1 = Label(text="1. "+allQuestion[0],fg="pink" ,bg="white")
        L1.place(x=30, y=60)
        L2 = Label(text="2. "+allQuestion[1],fg="pink" ,bg="white")
        L2.place(x=30, y=100)
        L3 = Label(text="3. "+allQuestion[2], fg="pink", bg="white")
        L3.place(x=30, y=140)
        L4 = Label(text="4. "+allQuestion[3], fg="pink", bg="white")
        L4.place(x=30, y=180)

    def hesapla():
        naiveBayes=0
        toplamOlasilik=0
        cevaplarString=cevaplar.get().strip().lower().split(",")
        if("evet" in cevaplarString[0]):
            naiveBayes+=1
        else:
            toplamOlasilik+=1
        if ("evet" in cevaplarString[1]):
            toplamOlasilik+=1
        else:
            naiveBayes+=1
        if ("evet" in cevaplarString[2]):
            toplamOlasilik+=1
        else:
            naiveBayes+=1
        if ("evet" in cevaplarString[3]):
            naiveBayes += 1
        else:
            toplamOlasilik += 1
        if(toplamOlasilik>naiveBayes):

            removeWidget()
            window.title("basicRandomNumber")
            window.minsize(600, 600)
            window.configure(bg="white")
            kosulSayisi=cevaplarString[4]
            kosullar = Entry(width=25)
            kosullar.place(x=150, y=70)
            NotKosullar = Label(text="lutfen kosullarin tek tek degerlerini sirayla (,) ile ayirarak bu kutucuga yaziniz",
                        fg="pink", bg="white", font="Verdana 15")
            NotKosullar.place(x=50, y=100)
            kosulluOlasiliklar = Entry(width=25)
            kosulluOlasiliklar.place(x=150, y=170)
            NotKosulluOlasiliklar = Label(text="lutfen A'ya gore B'nin kosullu olasililarini ustteki sirayla (,) ile ayirarak bu kutucuga yaziniz",
                        fg="pink", bg="white", font="Verdana 15")
            NotKosulluOlasiliklar.place(x=30, y=200)
            def toplamOlasilikHesapla():
                toplam=0
                kosullarString=kosullar.get().strip().lower().split(",")
                kosulluOlasiliklarString = kosulluOlasiliklar.get().strip().lower().split(",")
                for x in range(int(kosulSayisi)):
                    toplam+=float(kosullarString[x])*float(kosulluOlasiliklarString[x])

                tkinter.messagebox.showinfo(title="toplam OLasilik", message=str(toplam))

            gonder = Button(text="gonder", command=toplamOlasilikHesapla, fg="pink", bg="white")
            gonder.place(x=150, y=230)


        else:
            removeWidget()
            window.title("basicRandomNumber")
            window.minsize(600, 600)
            window.configure(bg="white")
            kosulSayisi = cevaplarString[4]
            kosullar = Entry(width=25)
            kosullar.place(x=150, y=70)
            NotKosullar = Label(
                text="lutfen kosullarin tek tek degerlerini sirayla (,) ile ayirarak bu kutucuga yaziniz",
                fg="pink", bg="white", font="Verdana 8")
            NotKosullar.place(x=50, y=100)
            kosulluOlasiliklar = Entry(width=25)
            kosulluOlasiliklar.place(x=150, y=170)
            NotKosulluOlasiliklar = Label(
                text="lutfen A'ya gore B'nin kosullu olasililarini ustteki sirayla (,) ile ayirarak bu kutucuga yaziniz",
                fg="pink", bg="white", font="Verdana 8")
            NotKosulluOlasiliklar.place(x=30, y=200)
            sart = Entry(width=5)
            sart.place(x=450, y=10)
            sartLabel = Label(
                text="Hangi sartin bayesini bulmak istersin kosul olasiliginin sirasina gore yaz",
                fg="pink", bg="white", font="Verdana 8")
            sartLabel.place(x=30, y=10)

            def bayesHesapla():
                toplam=0
                kosullarString = kosullar.get().strip().lower().split(",")
                kosulluOlasiliklarString = kosulluOlasiliklar.get().strip().lower().split(",")
                sartInt=int(sart.get())-1
                for x in range(int(kosulSayisi)):
                    toplam += float(kosullarString[x]) * float(kosulluOlasiliklarString[x])
                toplam=(float(kosullarString[sartInt]) * float(kosulluOlasiliklarString[sartInt]))/toplam

                tkinter.messagebox.showinfo(title="toplam OLasilik", message=str(toplam))

            gonder = Button(text="gonder", command=bayesHesapla, fg="pink", bg="white")
            gonder.place(x=150, y=230)


    sorular()
    geri = Button(text="<--", fg="pink", bg="white", highlightthickness=0, command=main)
    geri.place(x=10, y=10)
    cevaplar = Entry(width=25)
    cevaplar.place(x=300, y=220)
    Not = Label(text="lutfen tum cevaplari sirasiyla aralarinda (,) ile ayirarak bu kutucuga yaziniz", fg="white", bg="black",font="Verdana 8")
    Not.place(x=200,y=260)
    gonder = Button(text="gonder", command=hesapla, fg="pink", bg="white")
    gonder.place(x=510, y=217)

def kesikliRasgeleDegisenlerinDagilimi():
    removeWidget()
    window.title("basicRandomNumber")
    window.minsize(800, 600)
    window.configure(bg="white")
    allQuestion=["Duzgun dagilima sahip mi veya esit olasiliga sahiptir ifadesi geciyor mu","Deneyde sadece 2 sonuc var 0 ya da 1 olma olasiligini soruyorsa","Belli bir deneme sayisindan sonra (k) sayida  basarili olma olasiligini soruyor mu ","Belli bir deneme sonrasinda ilk basarili olma olasiligini soruyor mu ","Belli bir deneme sayisindan sonra (k) sayida  basariya ulasmak icin gereken denemeye sayisi modelliyor mu","Soru icinde λ isareti geciyor mu "]
    L1 = Label(text="1. " + allQuestion[0], fg="pink", bg="white")
    L1.place(x=30, y=20)
    L2 = Label(text="2. " + allQuestion[1], fg="pink", bg="white")
    L2.place(x=30, y=50)
    L3 = Label(text="3. " + allQuestion[2], fg="pink", bg="white")
    L3.place(x=30, y=80)
    L4 = Label(text="4. " + allQuestion[3], fg="pink", bg="white")
    L4.place(x=30, y=110)
    L5 = Label(text="5. " + allQuestion[4], fg="pink", bg="white")
    L5.place(x=30, y=140)
    L6 = Label(text="6. " + allQuestion[5], fg="pink", bg="white")
    L6.place(x=30, y=170)
    NotKosullar = Label(text="Bu seceneklerden hicbiri degil ise hipergeometrik dagilimdir ",
                        fg="pink", bg="white", font="Verdana 8")
    NotKosullar.place(x=30, y=200)
    cevaplar = Entry(width=5)
    cevaplar.place(x=200, y=230)
    def yazdir():
        cevap=cevaplar.get()
        if(cevap=="1"):
            tkinter.messagebox.showinfo(title="toplam OLasilik", message="Duzgun Dagilim")
        if (cevap == "2"):
            tkinter.messagebox.showinfo(title="toplam OLasilik", message="Bernoulli Dagilim")
        if (cevap == "3"):
            tkinter.messagebox.showinfo(title="toplam OLasilik", message="Binom dagilim")
        if (cevap == "4"):
            tkinter.messagebox.showinfo(title="toplam OLasilik", message="Geometrik Dagilim")
        if (cevap == "5"):
            tkinter.messagebox.showinfo(title="toplam OLasilik", message="Negatif Binom Dağılımı")
        if (cevap == "6"):
            tkinter.messagebox.showinfo(title="toplam OLasilik", message="Passion Dagilim")


    gonder = Button(text="gonder",command=yazdir, fg="pink", bg="white")
    gonder.place(x=250, y=227)



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
    window.minsize(600, 600)
    window.configure(bg="white")

    minLabel = Label(text="minimum sayiyi giriniz :",fg="pink" ,bg="white")
    minLabel.place(x=10, y=100)

    minInput = Entry(width=6)
    minInput.place(x=200, y=100)

    geri = Button(text="<--", fg="pink", bg="white", highlightthickness=0, command=main)
    geri.place(x=10, y=10)

    maxLabel = Label(text="maxsimum sayiyi giriniz :" ,fg="pink" ,bg="white")
    maxLabel.place(x=10, y=150)
    maxInput = Entry(width=6)
    maxInput.place(x=200, y=150)

    nLabel = Label(text="kac tane deger uretilecek:" ,fg="pink" ,bg="white")
    nLabel.place(x=10, y=200)
    nInput = Entry(window, width=6)
    nInput.place(x=200, y=200)

    hesapla = Button(text="hesapla", command=createRandomNubmer ,fg="pink" ,bg="white")
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


    window.wm_minsize(600,600)
    window.configure(background="white")
    window.title("systematicNumber")

    maxLabel=Label(text="Evrenin boyutunu giriniz :" ,bg="pink",fg="white")
    maxLabel.place(x=10,y=100)
    maxInput=Entry(width=6)
    maxInput.place(x=210,y=100)

    geri = Button(text="<--", fg="white", bg="black", highlightthickness=0, command=main)
    geri.place(x=10, y=10)

    nLabel = Label(text="Kac tane deger uretilecek:", fg="pink", bg="white")
    nLabel.place(x=10, y=150)
    nInput = Entry(window, width=6)
    nInput.place(x=210, y=150)

    hesapla = Button(text="Hesapla",command=createNumber, fg="pink", bg="white")
    hesapla.place(x=200, y=200)

    nInput.bind('<Return>', createNumber)
    hesapla.bind('<Return>', createNumber)
    maxInput.bind('<Return>', createNumber)


def floatVeriler():

    removeWidget()
    datas =[]





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


        dortteBirlikList=[]
        n1=N/4
        n2=(3*N)/4
        count1=0
        count2=0
        for x in EF:

            if n1<x:
                break
            count1 += 1

        for x in EF:
            if n2<x:
                break
            count2 += 1

        if count1 == 0:
            j1 = n1
        else:
            j1 = n1 - EF[count1 - 1]
        if count2 == 0:
            j2 = n2
        else:
            j2 = n2 - EF[count2 - 1]
        dortteBirlikList.append(((j1*H)/frekans[count1])+sinifMinDeger[count1])
        dortteBirlikList.append(((j2*H)/frekans[count2])+sinifMinDeger[count2])
        print(f"count1 {count1} --count2 {count2} -- frekans count 1 {frekans[count1]} -- frekans count 2 {frekans[count2]} -- sinifmindeger 1 {sinifMinDeger[count1-1]} sinif min deger 2 {sinifMinDeger[count2-1]}  j1 {j1}  j2 {j2}")

        tkinter.messagebox.showinfo(title="Dortte Birlik ",message=f"Q1 : {dortteBirlikList[0]}  "
                                                                    f"Q3 : {dortteBirlikList[1]}")




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

    window.minsize(600,600)
    labelData=Label(text="verileri giriniz :",bg="white",fg="pink")
    labelData.place(x=30,y=70)
    inputData=Entry(width=6)
    inputData.place(x=150,y=70)

    addButton=Button(text="ekle",fg="pink",bg="white",command=veriEkle)
    addButton.place(x=230,y=50)



    geri = Button(text="<--", fg="pink", bg="white",highlightthickness=0,command=main)
    geri.place(x=10, y=10)

    basitSeriButton = Button(text="basit seri", fg="pink", bg="white", command=basitSeri)
    basitSeriButton.place(x=10, y=180)

    frekansSeriButton = Button(text="frekans seri", fg="pink", bg="white", command=frekansSeri)
    frekansSeriButton.place(x=120, y=180)

    tabloButton = Button(text="tablo", fg="pink", bg="white", command=tablo)
    tabloButton.place(x=250, y=180)


    hoGo = Button(text="H.O - G.O", command=hoGo,fg="pink",bg="white")
    hoGo.place(x=220, y=230)

    varyansSapmaOms = Button(
text="""aritmetik,mod,medyan
varyans,sapma,OMS
baskililik,carpiklik,degisim""", command=carbasdeg,fg="pink",bg="white")
    varyansSapmaOms.place(x=10, y=230)

    inputData.bind('<Return>', veriEkle)


def intVeriler():
    removeWidget()
    datas = []



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

        dortteBirlikList = []
        n1 = N / 4
        j1=0
        j2=0
        n2 = (3 * N) / 4
        count1 = 0
        count2 = 0
        for x in EF:

            if n1 < x:
                break
            count1 += 1

        for x in EF:
            if n2 < x:
                break
            count2 += 1
        if count1==0:
            j1=n1
        else:
            j1 = n1 - EF[count1 - 1]
        if count2==0:
            j2=n2
        else:
            j2 = n2 - EF[count2 - 1]
        dortteBirlikList.append(((j1 * H) / frekans[count1]) + sinifMinDeger[count1])
        dortteBirlikList.append(((j2 * H) / frekans[count2]) + sinifMinDeger[count2])

        tkinter.messagebox.showinfo(title="Dortte Birlik ", message=f"Q1 : {dortteBirlikList[0]}  "
                                                                f"Q3 : {dortteBirlikList[1]}")


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




    window.minsize(600, 600)
    labelData = Label(text="verileri giriniz :", bg="white", fg="pink")
    labelData.place(x=30, y=70)
    inputData = Entry(width=6)
    inputData.place(x=150, y=70)

    addButton = Button(text="ekle", fg="pink", bg="white", command=veriEkle)
    addButton.place(x=230, y=50)



    geri = Button(text="<--", fg="pink", bg="white", highlightthickness=0, command=main)
    geri.place(x=10, y=10)

    basitSeriButton = Button(text="basit seri", fg="pink", bg="white", command=basitSeri)
    basitSeriButton.place(x=10, y=180)

    frekansSeriButton = Button(text="frekans seri", fg="pink", bg="white", command=frekansSeri)
    frekansSeriButton.place(x=120, y=180)

    tabloButton = Button(text="tablo", fg="pink", bg="white", command=tablo)
    tabloButton.place(x=250, y=180)

    hoGo = Button(text="H.O - G.O", command=hoGo,fg="pink",bg="white")
    hoGo.place(x=220, y=230)

    varyansSapmaOms = Button(
text="""aritmetik,  mod,     medyan
varyans,        sapma,       OMS
carpiklik,    baskililik,     degisim""", command=carbasdeg,fg="pink",bg="white")
    varyansSapmaOms.place(x=10, y=220)



    inputData.bind('<Return>', veriEkle)
def main():
    removeWidget()
    window.title("Olasilik")
    window.configure(background="white")
    window.minsize(width=800,height=800)

    basicRandomNumberButton=Button(text="basit rasgele sayilar",command=basicRandomNumber,fg="pink",bg="white")
    basicRandomNumberButton.place(x=50,y=200)

    systematicNumberButton=Button(text="sistematik rasgele sayilar",command=systematicNumber,fg="pink",bg="white")
    systematicNumberButton.place(x=200,y=260)

    float = Button(text="float sayilar", command=floatVeriler, fg="pink", bg="white")
    float.place(x=50, y=280)

    int = Button(text="intteger sayilar", command=intVeriler, fg="pink", bg="white")
    int.place(x=200, y=330)


    naivebayesToplamOlasilikButton = Button(text="naive bayes & toplam olasilik", command=naiveBayesToplamOLasilik, fg="pink", bg="white")
    naivebayesToplamOlasilikButton.place(x=50, y=130)

    kesikliRasgeleDegisenlerinDagilimiButton = Button(text="kesikli Rasgelese Degisenlerin Dagilimi",command=kesikliRasgeleDegisenlerinDagilimi,
                                      fg="pink", bg="white")
    kesikliRasgeleDegisenlerinDagilimiButton.place(x=50, y=50)

    window.mainloop()

main()