class icecekler():
    def __init__(self , ismi , fiyati,su,kahve,sut):
        self.kahveIsmi=ismi
        self.Fiyat=fiyati
        self.malzemeler={
            "su": su,
            "kahve":kahve,
            "sut":sut
        }
        
        
    
        

class menu():
    icecekler=["latte","espresso","su"]
    
    def __init__(self) :
        self.icecek=[
            icecekler("latte",15,200,2,200),
            icecekler("espresso",20,400,4,0),
            icecekler("su",5,500,0,0)
        ]
        
        
    def kahveAra(self,kahveIsmi):
        for oge in self.icecek:
            if(oge.kahveIsmi==kahveIsmi):
                return oge
        return -1
        
        
    def kahveleriGoster(self):
        print("iceceklerimiz :")
        for x in self.icecekler:
            print(x)