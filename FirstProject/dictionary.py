# plakalar = {"kocaeli ": 41 , "istanbul" : 34 }

# plakalar["rize"]=53
# plakalar["izmir"]=36 

# plakalar["izmir"]=35 
# print(plakalar)

# ogrenciler ={
#     100:{
#         "ad":"cinar",
#         "soyad":"turan",
#         "yas":4
#     },
#     101:{
#         "ad":"ada",
#         "soyad" : "bilge",
#         "yas" : 10
#     }
# }

# print(ogrenciler[100]["ad"])


urun = {}




# id=input(" id: ")
# ad=input(" ad: ")
# fiyat=input(" fiyat : ")

# urun[id]={
#     "ad":ad,
    
#     "fiyat":fiyat
#     }

# urunler= urun[id]

# print(f"urun id :   {id} + urun adi :   {urunler['ad']}  urun fiyati :  {urunler['fiyat']} ")


carObj =  {
    "marka": "Opel",
    "model": "corsa",
    "yil" :   2022  
}


for x in carObj.values():  # burda anahtarlar marka model yil oluyor diger turlu anahtalar bir tane old marka yazisinida ekranda goruyoruz
    print(x)
    
for x,y in carObj.items():
    print(x,y)
    
sonuc= "marka" in carObj
print(sonuc)  #anahtarlarda marka anahtari varmi kontrol eder

carObj["renk"]="kirmizi"

# carObj.pop("renk")    del ile de aynisini yaparsin ya da direk carObj yi silersin

carObj.popitem()    #son anahtari siler


print(carObj)


obj = carObj.copy()



obj["marka"]="bmw"

print(carObj)
print(obj)




a= int(input())
b=int(input())

print(a * b)