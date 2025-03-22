# name=str(input("ismmini yoz :"))
# surname=str(input("familiyani yoz :"))
# year=int(input("tug'ilgan yilni yoz :"))
# country=str(input("tug'ilgan joyin yoz :"))
# email=str(input("emailni yoz :"))
# tel=int(input("telefon raqamni yoz +998"))


# def obj(ism,familiya,yil,joy,em='',telefon=0):
    
#     if em and telefon:
#         n_o={"ism":ism,
#          "familiya":familiya,
#          "yil":yil,
#          "joy":joy,
#          "em":em,
#          "tel":(+9989,telefon),
#          "yosh":2025-yil
#          } 
#     elif em:
#           n_o={"ism":ism,
#          "familiya":familiya,
#          "yil":yil,
#          "joy":joy,
#          "em":em,
#          "yosh":2025-yil
#          }     
#     elif telefon:
#          n_o={"ism":ism,
#          "familiya":familiya,
#          "yil":yil,
#          "joy":joy,
#          "tel":(f"+9989{telefon}"),
#          "yosh":2025-yil
#          }       
       
    
    
#     return n_o;


# a=obj(name,surname,year,country,email,tel)

# print(a)
    
    
    
################################################################################################################################################



# def obj(ism,familiya,yil,joy,em='',telefon=0):
    
#     if em and telefon:
#         n_o={"ism":ism,
#          "familiya":familiya,
#          "yil":yil,
#          "joy":joy,
#          "em":em,
#          "tel":(f"+9989{telefon}"),
#          "yosh":2025-yil
#          } 
#     elif em:
#           n_o={"ism":ism,
#          "familiya":familiya,
#          "yil":yil,
#          "joy":joy,
#          "em":em,
#          "yosh":2025-yil
#          }     
#     elif telefon:
#          n_o={"ism":ism,
#          "familiya":familiya,
#          "yil":yil,
#          "joy":joy,
#          "tel":(f"+9989{telefon}"),
#          "yosh":2025-yil
#          }       
       
    
    
#     return n_o;

# mijozlar=[]

# while True:
#    name=str(input("ismmini yoz :"))
#    surname=str(input("familiyani yoz :"))
#    year=int(input("tug'ilgan yilni yoz :"))
#    country=str(input("tug'ilgan joyin yoz :"))
#    email=str(input("emailni yoz :"))
#    tel=int(input("telefon raqamni yoz +998")) 
       
#    a=obj(name,surname,year,country,email,tel)   
#    mijozlar.append(a)
#    t=input("yana malumot qo'shasizmi ? (ha/yoq)")
   
#    if t=='ha':
#        continue
#    else:
#        break
   
   
   
# for val in mijozlar:
 
#   print(f"ism:{val["ism"]}\nfamiliya:{val["familiya"]}\ntug'ilgan yili:{val["yil"]}\nemail:{val["em"]}\n{val["tel"]}\nyosh:{val["yosh"]}\n")   
       
       
       
# def bign(n1,n2,n3):
#     if n1<n2<n3:
#         return n3
#     elif n2<n3<n1:
#         return n1 
#     elif n3<n1<n2:
#         return n2
#     elif n2==n3 and n3==n1:
#         return "teng"
#     elif n2 == n3 and n1>n3 :
#        return n1
#     elif n2==n1 and n3>n1:
#         return n3
#     elif n1==n3 and n2>n1:
#         return n2
#     elif n2 == n3 and n1<n3 :
#         return "2 son teng"
#     elif n2==n1 and n3<n1:
#         return "2 son teng"
#     elif n1==n3 and n2<n1:
#        return "2 son teng"  
#     else:
#         print("xato")    
        
        
# son1=int(input("son1 yoz :"))     
# son2=int(input("son2 yoz :"))           
# son3=int(input("son3 yoz :"))


# a=bign(son1,son2,son3)

# print (a)


            
                   
# rad=float(input("aylanai radiusni yoz :"))

# def m(r):
#     d=2*r;
#     p=d*3.14;
#     s=(3.14*d**2)/4
    
#     return {"diametr":d,"perimetr":p,"yuz":s}
                    
                   
              
# print(m(rad))         


# son1=int(input("son boshin yoz :"))
# son2=int(input("son2 oxirni yoz :"))

# def tub_sonlar(mn,mx):
#     son=[]
#     tub=[]
#     while mn<mx+1:
#         son.append(mn)
#         mn+=1
    
#     for val in son:
#         n=True
#         if val == 2 :
#             n=True
#         elif val ==1:
#             n=False    
#         else :
#             for v in range(2,val,1):
            
#                 if val%v==0:
                   
#                     n=False
                   
#         if n:
#             tub.append(val)
          
#     return tub  
                            
          
# a=tub_sonlar(son1,son2)
# print(a)   

##################################################################################################################################################

# son = int ( input ( "nechga qadar son fibanachi soni kerak :"))
# f=[]
# def fib(son,s=1,s2=1):
#     if son>s:
#         a=s+s2
#         f.append(a)
#         return fib(son,a,s)
#     else:
#         return f
        
# a=fib(son)
# print(a)    
    
    
    
           
                     
             
            
        
   
     
        
        
         
        
    
     
          
             
     