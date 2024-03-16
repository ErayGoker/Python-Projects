class Question():
    text=[]
    answer=[]
    questionAndAnswer={}
    
    def __init__(self,text):
        
        self.questionAndAnswer.update(text)
        

    def cevir(self):        
        for x in self.questionAndAnswer:
            self.text.append(x)
            
            
        for y in self.questionAndAnswer.values():
            self.answer.append(y)    
    
        
    def kontrol(self,answer , index):
        if(self.answer[index]==answer):
            return True
        return False    
    
    
    
    
    
        
        
        
      
      
    
    
        
        