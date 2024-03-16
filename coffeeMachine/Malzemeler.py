class Malzeme():
    malzeme= {
            'water':300,
            "milk":200,
            'coffee':100,
            'money':0
        }

    def report(self):
        print(f"""
            water :{self.water}
            milk :{self.milk}
            coffee :{self.coffee}
            money :{self.money}
        
        """)

    def urunKontrol(self,kahve):
        kontrol=True
        for x in self.malzeme:
            if(kahve[x] <= self.malzeme[x]):
                None
            else:
                kontrol=False
                print("makinadaki malzemeler eksik ")
                break
        for x in self.malzeme:
            if(kontrol==True):
              self.malzeme[x]-=kahve[x]

        if(kontrol==True):
            print("kahveniz hazirlaniyor")


