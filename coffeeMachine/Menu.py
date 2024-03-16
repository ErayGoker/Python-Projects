class Menu():
    kahveler = [
        {
            'isim': "expresso",
            'water': 75,
            'milk': 50,
            'coffee': 60,
            'money': 2
        },
        {
            'isim': "latte",
            'water': 60,
            'milk': 70,
            'coffee': 80,
            'money': 2.5
        },
        {
            'isim': "cappucino",
            'water': 40,
            'milk': 80,
            'coffee': 70,
            'money': 3
        }
    ]
    def __init__(self):

        print("kahvelerimiz : 1.expresso, 2.latte , 3.cappucino  ")

    def kahveniSec(self):
        kahveSecimim=input("Istediginiz kahvenin ismini giriniz : ")
        if (kahveSecimim=="latte"):
            kahveSecimim=2
        elif(kahveSecimim=="cappucino"):
            kahveSecimim=3
        else:
            kahveSecimim=1
        return self.kahveler[kahveSecimim-1]
