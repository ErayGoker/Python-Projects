# print('eray','goker',sep='/')
# print(*'TBMM')
# A=4
# B=6
# print(f"{A} sayisi ile {B} sayisi toplami {A+B} eder")


# print("oyuncu kaydetme programina hosgeldiniz")

# ad = input("oyuncu adi : ")
# numarasi = int(input("oyuncu numarasi : "))
# takimi = input("oyuncunun takimi : ")

# oyuncuBilgileri = (ad,numarasi,takimi)
# oyuncuBilgileri1={
#     "oyuncu adi":ad,
#     "oyuncu numarasi":numarasi,
#     "oyuncunun takimi":takimi 
# }

# print("oyuncu kaydediliyor")

# print("oyuncunun adi : " , oyuncuBilgileri[0] , "\noyuncunun numarasi : " , oyuncuBilgileri[1] ,
# "\noyuncunun takimi : ", oyuncuBilgileri[2] )

# for x,y in oyuncuBilgileri1.items():
#     print(x,y)


# birinciSayi=int(input("birnici sayiyi giriniz : "))
# ikinciSayi=int(input("ikinci sayiyi giriniz : "))
# ucuncuSayi=int(input("ucuncu sayiyi giriniz : "))
# print("birinci sayi : {} \t ikinci sayi : {} \t ucuncu sayi: {}\n ucunun toplami : {}".format(birinciSayi,ikinciSayi,ucuncuSayi,(birinciSayi+ikinciSayi+ucuncuSayi)) )


# print("""
#       Hesap Makinesine hosgeldiniz
      
#       islemler:
      
#       1.toplama islemi
      
#       2.cikarma islemi
      
#       3 carpma islemi 
      
#       4.bolme islemi
      
    
#       """)

# islem=int(input("islemi seciniz : "))

# birinciSayi=int(input("birnici degeri giriniz"))

# ikinciSayi = int(input("ikinci sayiyi giriniz"))

# if islem==1:
#     print(birinciSayi+ikinciSayi)
# elif islem==2:
#     print(birinciSayi-ikinciSayi)    
# elif islem==3:
#     print(birinciSayi*ikinciSayi)  
# elif islem==4:
#     print(birinciSayi/ikinciSayi)  
# else:
#     print("lutfen gecerli islem giriniz")



# def asalMi(sayi):
#     for i in range(2,sayi+1):
#         for j in range(2,i):
#             if(i!=j and i % j == 0):
                
#                 print(f"{i} sayisi asal degildir") 
#                 break
                
# asalMi(15)


# def encode(mesaj,shift):
#     alfabe=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z"]
#     mesaj1=[]
#     for i in mesaj:
#         mesaj1 += i

#     for i in mesaj1:
       
        
#         mesaj1[indexNum]=alfabe[indexNum + shift]

#         return mesaj1




# shift = int(input("atlama sayisini giriniz : "))

# print(encode("hosgeldiniz", shift))


# try: 
#    x=10
#    y=0
#    print(x/y)
# except Exception as e:
#     print(e)


# class Comment:
#     def __init__(self, userName,text,likes=0,dislike=0):
#         self.userName=userName
#         self.text=text
#         self.likes=likes
#         self.dislike=dislike
        
        
# p1=Comment("eray","cok iyi",100,5)
# p2=Comment("yasmin","cok iyi",50,4)
# p3=Comment("nilufer","cok iyi",200,6)
# p4=Comment("nilay","cok iyi",500,1)

# yorumlar = [(p1.userName,p1.text),(p2.userName,p2.text),(p3.userName,p3.text),(p4.userName, p4.text)]

# for i,j in yorumlar:
#     print(f"isim : {i} \t yorum : {j} ")


# class Banka():
#     def __init__(self,ad,miktar=0) -> None:
#         self.ad=ad
#         self.miktar=miktar
        
#     def getMiktar(self):
#         return self.miktar
    
#     def setMiktar(self,miktar):
#         if(miktar<0):
#             raise Exception("- deger yatiramazsiniz")
#         else:
#             self.miktar+=miktar
            
            
#     Banka=property(setMiktar,getMiktar)
    
    
# banka=Banka("Eray",100)

# banka.setMiktar(500)


# print(banka.miktar)