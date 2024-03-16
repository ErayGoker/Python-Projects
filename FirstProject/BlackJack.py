import random

kartlar = [11,2,3,4,5,6,7,8,9,10,10,10,10]



print("BlackJack'a hosgeldiniz\n\n")
giris=input("Oyuna girmek icin S tusuna basiniz cikmak icin E tusuna basiniz : ")

def kartDagit():
    kart=int(random.random()*13)
    return kartlar[kart]
     

while(giris=='S'):
    
    bilgisayarinKartlari=[kartDagit(),kartDagit()]
    oyuncuKartlari=[kartDagit(),kartDagit()]
    print("Bilgisayarin kartlari : ", bilgisayarinKartlari[0])
    print("Oyuncu kartlari : " , oyuncuKartlari[0] , "  " , oyuncuKartlari[1])
    if((oyuncuKartlari[0]+oyuncuKartlari[1])>21):
        if(oyuncuKartlari[0]==11  ):
            oyuncuKartlari[0]=1
        elif(oyuncuKartlari[1]==11  ):
            oyuncuKartlari[1]=1
        else:
            print("Bilgisayarin kartilari toplami : " , (bilgisayarinKartlari[0] + bilgisayarinKartlari[1]),"\n")
            print("Oyuncu kartlari toplami : " , (oyuncuKartlari[1]+oyuncuKartlari[0]),"\n")
            oyuncuKartlari.clear()
            bilgisayarinKartlari.clear()
            giris=input("Oyunu kaybettiniz devam etmek icin S tusuna basınız")
    elif((oyuncuKartlari[0]+oyuncuKartlari[1])<21):       
            kartIste=input("kart istemek icin Y tusuna istemezseniz N tusuna basiniz")
            if(kartIste=='Y'):
                oyuncuKartlari.append(kartDagit())
                for a in oyuncuKartlari:
                    toplam=0
                    toplam+=a
                    if(toplam>21):
                        print("Bilgisayarin kartilari toplami : " , (bilgisayarinKartlari[0] + bilgisayarinKartlari[1]),"\n")
                        print("Oyuncu kartlari toplami : " , toplam,"\n")
                        oyuncuKartlari.clear()
                        bilgisayarinKartlari.clear()
                        giris=input("Oyunu kaybettiniz devam etmek icin S tusuna basınız")    
                    else:
                        for a in oyuncuKartlari:
                            toplam=0
                            toplam+=a
                        if((bilgisayarinKartlari[0]+bilgisayarinKartlari[1])>toplam):
                            print("Bilgisayarin kartilari toplami : " , (bilgisayarinKartlari[0] + bilgisayarinKartlari[1]),"\n")
                            print("Oyuncu kartlari toplami : " , toplam,"\n")
                            oyuncuKartlari.clear()
                            bilgisayarinKartlari.clear()
                            giris=input("Oyunu kaybettiniz devam etmek icin S tusuna basınız")  
                        else:
                            print("Bilgisayarin kartilari toplami : " , (bilgisayarinKartlari[0] + bilgisayarinKartlari[1]),"\n")
                            print("Oyuncu kartlari toplami : " , toplam,"\n")
                            oyuncuKartlari.clear()
                            bilgisayarinKartlari.clear()    
                            giris=input("Oyunu kazandiniz devam etmek icin S tusuna basınız")  
            
            if(kartIste=="N"):
                for a in oyuncuKartlari:
                    toplam=0
                    toplam+=a
                if((bilgisayarinKartlari[0]+bilgisayarinKartlari[1])>toplam):
                    print("Bilgisayarin kartilari toplami : " , (bilgisayarinKartlari[0] + bilgisayarinKartlari[1]),"\n")
                    print("Oyuncu kartlari toplami : " , toplam,"\n")
                    oyuncuKartlari.clear()
                    bilgisayarinKartlari.clear()
                    giris=input("Oyunu kaybettiniz devam etmek icin S tusuna basınız")  
                else:
                    print("Bilgisayarin kartilari toplami : " , (bilgisayarinKartlari[0] + bilgisayarinKartlari[1]),"\n")
                    print("Oyuncu kartlari toplami : " , toplam,"\n") 
                    oyuncuKartlari.clear()
                    bilgisayarinKartlari.clear()
                    giris=input("Oyunu kazandiniz devam etmek icin S tusuna basınız")  
            
                
                
                  

    
