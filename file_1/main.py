# fayl=open("text.txt")
# txt=fayl.read()
# print(txt)
# fayl.close()
#######################################################################################
# fayl=open("pi_million_digits.txt")
# pi=fayl.read()
# pi=pi.rstrip()
# pi=pi.replace("\n",'')
# pi=float(pi)
# print(pi[:50])

# fayl.close()
######################################################################################

# with open("pi_million_digits.txt") as fayl:
#     pi=fayl.read().rstrip().replace("\n",'')
#     # pi=float(pi)
# # print(pi[:50])   

# mybith="01112004"
# son=pi.find(mybith)

# if son != -1:
#     print("bor bu son qatori:",son) 
# else:
#     print("yoq")   

########################################################################################
    

# faylnom="ilhom"
# with open(faylnom,"w") as fayl:
#     fayl.write("salom dunyo")


##################################################################################################
# import pickle   
# import os
# with open ("pi_million_digits.txt") as f:
#     pi=f.read().replace("\n","").rstrip()
    
    
# nw="yangipi.pkl"
# print(len(pi))
# with open(nw,"wb") as nf:
#     pi=list(pi)
#     pickle.dump(pi,nf)
# with open(nw,"rb") as nff:
#     p=pickle.load(nff) 
     
##########################################################################################################


name=input("ism nima:")

name+=".txt"

with open(name,"a") as fayl:
    b=True
    while(b):
        nom=input("malumot yoz aga yozmoqchi bo'lamsan (yoq) deb yoz:")
        if nom!="yoq":
            fayl.write(nom)
        else:
            b=False    
        
    
    
      
    