from QuestionModel import Question
from Data import question_data
import time


for x in question_data:
    newQuestion = Question(x)

newQuestion.cevir()

print(newQuestion.text)
    
index=0
dogru=0
yanlis=0
print("soru makinesine hosgeldiniz")

while(True):
    
    print(f"{index+1} sorunuz : {newQuestion.text[index]}")
    answer=input("lutfen cevabi giriniz : ")
    print("cevap kontrol ediliyor ...")
    time.sleep(1)
    if(newQuestion.kontrol(answer,index)):                                                      # text.pop() yaparak her yeri sifir yaparakta yapabilinir
        dogru+=1
        print(f"cevabiniz dogru {dogru}/{yanlis}")
        
    else:
        yanlis+=1
        print(f"cevabiniz yanlis {dogru}/{yanlis}")
    
    index+=1
    
    if(index==len(newQuestion.text)):
        break
    
        


