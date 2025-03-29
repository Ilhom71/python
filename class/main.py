# class user:
#     def __init__(self,ism,familiya,yosh,email,parol):
#         self.name=ism
#         self.surname=familiya
#         self.yosh=yosh
#         self.email=email
#         self.passwrod=parol
#     def getname(self):
#         return self.name
#     def age(self):
#         return self.age
#     def em(self):
#         return self.email
#     def info_user(self):
#         return f"men {self.name} familiyam {self.surname} yoshim {self.yosh} \t email {self.email} parol {self.passwrod}"
    
    
# foydalanuvchi1=user("ilhom","mirtojiyev",20,"any@gamil.com","1234566")
    
# print(foydalanuvchi1.info_user())


######################################################################################################################################

class test :
    def __init__(self,name,age):
        self.ism=name
        self.yosh=age
    def name(self):
        return self.ism
    def age(self):
        return self.yosh
    
    
print("malumot kiritin men uni class joylayman :")    
while True:
    name=input("ismni yozin :")
    age=input("yoshni yozin :")
    
    if age!="":
        
      age=int(age)
    

        
    
    
    
    if name!="" and  age>=0:
        f=test(name,age)
        print(f.name())
        print(f.age())
        break
    else:
        continue
    
    
        
        
    
            