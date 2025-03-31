##################################################################################################################################################
# class talaba:
  
#     def __init__(self,ism,familiya,yosh,passport):
#         self.ism=ism
#         self.familiya=familiya
#         self.yosh=yosh
#         self.passport=passport
        

# class fan(talaba):
#       def  __init__(self,ism,familiya,yosh,passport,id):    
#           super().__init__(ism,familiya,yosh,passport)
#           self.bosqich=1
#           self.id=id
#           self.fan=[]
#       def get_passport(self):
#           """id olish"""   
#           return self.id
#       def get_bosqich(self):
#           return self.bosqich
      
#       def info(self):
#          return f"ism:{self.ism}\nfamiliya:{self.familiya}\nyosh:{self.yosh}\nbosqich:{self.bosqich}"
#       def fan_yoz(self,fan):
#           self.fan.append(fan)
#       def fanlar_info(self):
#           f=f"ism :{self.ism}\nfamiliya:{self.familiya}\n" 
#           for v in self.fan:
#               f+=f"fan:{v}\n"
#           return f 
#       def remove_fan(self,fan):
#           if fan in self.fan:
#               self.fan.remove(fan)
#           else:
#               print(f"siz bu {fan} fanni yozmagansiz") 
                
               
          
     
     
     
# men=fan("ilhom","mirtojiyev",20,1111111,3)
# men.fan_yoz("matematika")
# men.fan_yoz("english")
# men.fan_yoz("it")
# men.remove_fan("ona-tili")
# men.remove_fan("it")

# print(men.fanlar_info())
# # print(men.info())       
  
###############################################################################################################################################          
class shaxs:
    def __init__(self,ism,familiya,passport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
    def get_info(self):
        info=f"ism:{self.ism}\nfamiliya:{self.familiya}\npassport:{self.passport}\ntug'ilgan yil:{self.tyil}"
        return info
    def get_age(self,yil):
        return yil-self.tyil      
    
    
class mijoz(shaxs):
    def __init__(self,ism,familiya,passport,tyil,joy,market,narsalar):
        super().__init__(ism,familiya,passport,tyil)
        self.joy=joy
        self.market=market
        self.narsalar=narsalar    
        
    def get_anyparm(self):
        return [self.market,self.narsalar,self.joy]
    def get_info(self):
        info=f"ism:{self.ism}\nfamiliya:{self.familiya}\npassport:{self.passport}\ntug'ilgan yil:{self.tyil}\nmarket:{self.market}\njoy:{self.joy}"
        return info
    
class professor(shaxs):
    def __init__(self,ism,familiya,passport,tyil,joy,daraja,fan):
        super().__init__(ism,familiya,passport,tyil)
        self.joy=joy
        self.daraja=daraja
        self.fan=fan 
    def get_info(self):
        info=f"ism:{self.ism}\nfamiliya:{self.familiya}\npassport:{self.passport}\ntug'ilgan yil:{self.tyil}\njoy:{self.joy}\ndarja:{self.daraja}\nfan:{self.fan}"
        return info    
        
class sotuvchi(shaxs):
      def __init__(self,ism,familiya,passport,tyil,joy,market_name,narsa):
          super().__init__(ism,familiya,passport,tyil)
          self.joy=joy
          self.market_name=market_name
          self.narsa=narsa
      def any_thing(self):
            return [self.joy,self.market_name,self.narsa]  
      def get_info(self):
        info=f"ism:{self.ism}\nfamiliya:{self.familiya}\npassport:{self.passport}\ntug'ilgan yil:{self.tyil}\nmarket nomi:{self.market_name}\nbuyumlar:{self.narsa}"
        return info      
          
class admin(shaxs):
    def __init__(self,ism,familiya,passport,tyil,daraja,malumot,holat="faol"):
        super().__init__(ism,familiya,passport,tyil)
        self.daraja=daraja
        self.malumot=malumot
        self.holat=holat
        
    def get_info(self):
        return f"ism:{self.ism}\nfamiliya:{self.familiya}\npassport:{self.passport}\ntug'ilgan yil:{self.tyil}\ndaraja:{self.daraja}\nmalumot:{self.malumot}"   
    def get_holat(self):
        return self.holat   
class foydalanuvchi(shaxs):
    def __init__(self,ism,familiya,passport,tyil,daraja,malumot,holat):
        super().__init__(ism,familiya,passport,tyil)
        self.daraja=daraja
        self.malumot=malumot
        self.holat=holat
    def get_info(self):
        return f"ism:{self.ism}\nfamiliya:{self.familiya}\npassport:{self.passport}\ntug'ilgan yil:{self.tyil}\ndaraja:{self.daraja}\nmalumot:{self.malumot}\nholat:{self.holat}" 
    def get_holat(self):
        return self.holat                  
          
        
        
        
# men=shaxs("ilhom","mirtojiyev",'0000001',2004)
# mijoz1=mijoz("ali","ahmadov","101010",2004,"toshkent","superbola",["kalit","kaptok","pul"])
# professor1=professor("porajon","karupsiyayev","99999999",1991,"toshkent",2,"ona tili")
# sotuvchi1=sotuvchi("miral","boyev","0000020",2000,"samarqand","katta bola ",["big boy","yellow boy ","green doll"])


# print(men.get_info(),"\n")
# print(mijoz1.get_info(),"\n")         
# print(professor1.get_info(),"\n") 
# print(sotuvchi1.get_info(),"\n") 

persons=[]

persons.append(admin("ilhom","mirtojiyev","090909",2004,"admin","web-dasturchi"))
persons.append(foydalanuvchi("ali","mirov","9999999",1999,"foydalanuvchi","talaba","block"))
persons.append(foydalanuvchi("husan","kamilov","9999999",1989,"foydalanuvchi","alkash","faol"))


for val in persons:
    
    if val.get_holat():
        if val.get_holat()=="block":
            print(val.ism,"<====bu odam xafli !!!!!!")
     
         
    
    print(val.get_info(),"\n")

                        
          