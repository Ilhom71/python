class shaxs:
    odamlar=0
    def __init__(self,ism,familiya,yosh,tyil,passpoert):
        shaxs.odamlar+=1
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        self.tyil=tyil
        self.__passpoert=passpoert
        
    def info(self):
        return f"ism:{self.ism}\nfamiliya:{self.familiya}\nyosh:{self.yosh}\ntug'ilgan yil:{self.tyil} \n"
    def getname(self):
        return self.ism
    def getpassport(self):
        return self.__passpoert
    def setpassport(self,passpoert2):
        self.__passpoert=passpoert2
    def setname(self,name):
        self.ism=name
    def set_surname(self,surname):
        self.familiya=surname
    def info_odamlar() :
        return shaxs.odamlar   
               


class talaba(shaxs):
    __talabalar=0
    def __init__(self,ism,familiya,yosh,tyil,passpoert,kurs,gpu):
        super().__init__(ism,familiya,yosh,tyil,passpoert) 
        self.kurs=kurs
        self.gpu=gpu
        self.fanlar=[]
        talaba.__talabalar+=1
    def setfan(self,fan):
        self.fanlar.append(fan)  
      
    def infofan(self):
        return self.fanlar 
    #bu method class lar bilan ishlashga yordam beradi 
    @classmethod
    def info_tson(cls):
        return cls.__talabalar
        
         
           
    
    
        
            
        