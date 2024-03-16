from Menu import icecekler,menu
from Maker import kahveYapici

print("kaahve makinasina hosgeldiniz")

menu=menu()

menu.kahveleriGoster()
    
secim=input("lutfen yukaridaki iceceklerden birini seciniz")


kahveYap=kahveYapici()

kahveYap.malzemeKontrolu(menu.kahveAra(secim).malzemeler)
kahveYap.yap(menu.kahveAra(secim).malzemeler)

print(kahveYap.malzemeler)



