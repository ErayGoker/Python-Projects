import Malzemeler
import Menu

print(f"""
    kahve makinesine hosgeldiniz 
        5 lira ve 10 lira ile calisir
    
""")
malzemeler=Malzemeler.Malzeme()
menu=Menu.Menu()
kontrol=True
while(kontrol):
    para=int(input("lutfen paranizi atiniz "))
    malzemeler.malzeme["money"]=para
    print(malzemeler.malzeme)
    malzemeler.urunKontrol(menu.kahveniSec())
