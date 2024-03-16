class kahveYapici():
    def __init__(self):
        self.malzemeler={
            "su":800,
            "kahve":15,
            "sut":800
        }
        
    def yap(self,icecek):
        for oge in self.malzemeler:
            self.malzemeler[oge]-=icecek[oge]
        
        print("iceceginiz hazir afiyet olsun ")
        
        
    def malzemeKontrolu(self,icecek):
        for oge in self.malzemeler:
            
            if(self.malzemeler[oge]<icecek[oge]):
               
                print("malzememiz eksik")
                return False
        
        print("iceceginiz hazirlaniyor")
        
            