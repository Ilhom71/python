

# class avto:
    
#     def __init__(self,model,rang,karbka,narh,yil,kilometr=0,joy="salon"):
#         self.model=model
#         self.rang=rang
#         self.karbka=karbka
#         self.narh=narh
#         self.yil=yil
#         self.kilometr=kilometr
#         self.joy=joy
        
#     def get_info(self) :
        
#         return f"mashina ruimmi :{self.model}\n rangi:{self.rang} \n narhi {self.narh} \n yilli:{self.yil}\n bosgan masofasi :{self.kilometr}km\n joy{self.joy}"
#     def up_km(self,km):
#         self.kilometr=km
               
           
# kobilt=avto("kobilt","qora","yoq",1500,2010,10,"toshkent")
# kobilt.up_km(100)

# print(kobilt.get_info())           


#################################################################################################################################################
n=0

class autosalon:
    
    def __init__(self,nom,manzil,boss,sotuv_avtomiblar):
        self.nom=nom
        self.manzil=manzil
        self.sotuv_avtomiblar=[sotuv_avtomiblar]
        self.boss=boss
        self.avto_son=0
        
    def avto_q(self,avtomobil,narhi=0,yil=0):
        avto={"nom":avtomobil,"narxi":narhi,"yil":yil}
        self.sotuv_avtomiblar.append(avto)
        self.avto_son+=1
        
    def avtomobils_info(self):
        
       a= self.sotuv_avtomiblar    
       for v in a:
           print(f"nom:{v["nom"]},\n narx :{v["narxi"]}\n yil:{v["yil"]}")
def methods(klass):
    return [method for method in dir(klass) if method.startswith("__") is False]       
           


uzavto=autosalon("uzavto","toshkent","ilhom",{"nom":"trkker","narxi":2000,"yil":2019})
uzavto.avto_q("kobilt",1500,2002)
uzavto.avto_q("malibu",2000,2018)
uzavto.avto_q("bmw",4000,2010)

uzavto.avtomobils_info()
# print(dir(autosalon)) 
# print(uzavto.__dict__)
# print(uzavto.__dict__.keys())       
# print(dir(str))
# print(dir(int))

# a=methods(uzavto)
# print(a)


     
   
           
           
    
        
        
              
        