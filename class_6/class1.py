class shaxs:
    def __init__(self,ism,familiya,yosh,joy="none"):
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        self.joy=joy
    def getname(self):
        return self.ism 
    def info(self):
        return f"ism:{self.ism}\nfamiliya:{self.familiya}\nyosh:{self.yosh}\njoy:{self.joy}"
    def __repr__(self):
        return f"ism:{self.ism}\nfamiliya:{self.familiya}\nyosh:{self.yosh}\njoy:{self.joy}"
    def __eq__(self,a):
        return self.kurs==a
    def __lt__(self,a):
        return self.kurs<a
    def __le__(self,a):
        return self.kurs<=a
    def __gt__(self,a):
        return self.kurs>a
    def __ge__(self,a):
        return self.kurs>=a
    def __ne__(self,a):
        return self.kurs1!=a
    
    
    
class talaba(shaxs):
    def __init__(self,ism,familiya,yosh,joy,kurs,idhuman):
        super().__init__(ism,familiya,yosh,joy)
        self.kurs=kurs
        self.__id=idhuman
    def getid(self):
        return self.__id        



          
        
       
        
       
class fan():
    def __init__(self,name):
        self.name=name
        self.talabalarson=0
        self.talabalar=[]
    def add(self,student):
        self.talabalar.append(student)
        self.talabalarson+=1
    def __getitem__(self,a):
        return self.talabalar[a]  
    def __setitem__(self,a,b):
        self.talabalar[a]=b 
    def __len__(self):
        return self.talabalarson
    def __add__(self,student):
          self.talabalar.append(student)
          self.talabalarson+=1
    def __sub__(self,id1):
        for val in self.talabalar:
            if val.getid() == id1:
                 self.talabalar.remove(val)
    def __call__(self,student):
        if student:
            for val in self.talabalar:
                if val==student :
                    return val
                else:
                    return  False
             
        else :
                return self.talabalar[:]
    
                     
           
                    
            
            
           
    
              
            
          
            

               