import random

canHakki=5

resim=['''
            +---+
            |   |
            O   |
          / | \ |
           / \  |
                |
       -------------
       
       ''','''
            +---+
            |   |
            O   |
          / | \ |
           /    |
                |
       -------------
       
       ''','''
            +---+
            |   |
            O   |
          / | \ |
                |
                |
       -------------
       
       ''','''
            +---+
            |   |
            O   |
          / |   |
                |
                |
       -------------
       
       ''','''
            +---+
            |   |
            O   |
            |   |
                |
                |
       -------------
        ''','''
            +---+
            |   |
            O   |
                |
                |
                |
       -------------
        ''']

cevapListesi = ["bardak","kalem","kahvalti","eglenmek"]

cevap=random.choice(cevapListesi)

cevapHarfleri = [i for i in cevap]

liste = []

for a in cevapHarfleri:
    liste+="_"


 
print(resim[5])
print(liste)
while('_' in liste and canHakki>0):
    
    

    tahmin = input("harf tahmin ediniz : ").lower()
    
    for i in range(len(cevapHarfleri)):
        if(cevapHarfleri[i]==tahmin):
            liste[i]=tahmin
       
    print(liste)
    
    if(tahmin not in cevapHarfleri):
        canHakki-=1
        print(resim[canHakki])
    
    if(not '_' in liste):
        print("kazandiniz")
        
    if(canHakki==0):
        print("kaybettiniz")
    
    

