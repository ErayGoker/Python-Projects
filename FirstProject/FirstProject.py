print(2+2)
print(type(2.6))

print(10**2)

print(10/2)     
print(10//2)  # yorum satiridir

urunA=5000
urunB=60.00
karakter="eray"

print(urunA+urunB)

print(float(urunA))
print(float(urunA))
print(karakter[-1])
print(karakter[0])
print(karakter[0:4])    # 0 dahil 4 dahil degil aradaki karakterleri yazdirir
print(karakter[::-1])   # bastan sona kadar git ama -1 er git dedik

print(len(karakter))  # karakter sayisini veriyor

print(karakter + str(urunA))


ad = "eray"
soyad = "goker"
yas=4

print("benim ismim {s} {n}".format(n=ad,s=soyad))
print("benim ismim {} {} . I'm {}".format(ad,soyad,yas))

print(f"benim ismim {ad} {soyad} . I'm {yas}")

print(len("kursAdi"))

webSite= "https://www.udemy.com/course/python-dersleri/learn/lecture/15939998#overview"


index= webSite.index("com")

print(webSite[index:index+3])

yeniDeger= webSite.replace("dersleri","dersler")

print(yeniDeger)

