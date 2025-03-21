# mahsulotlar=[]

# while True:
#     a=input("nima istaysiz\t")
#     mahsulotlar.append(a)
#     res=input("siz yana mahsulot olasizmi(ha/yoq)>>>")
#     if res=="ha":
#         continue
#     else:
#         break

# print("sizning mahsulotlaringiz")  
# for val in mahsulotlar:
#       print(val,"\t")
#################################################################################################################################################
# mahsulot=[]

# while True:
#     name=input("mahsulotni nomi>>>")
#     narxi=input("mahsulotni narxi>>")
#     sana=input("mahsulot sanasi")
#     mahsulot.append({"nom":name,"narx":narxi,"sana":sana})
    
#     res=input("yana nimadur olasizmi ? (ha/yoq)")
    
#     if res=="ha":
#         continue
#     else:
#         break
    
    
# for val in mahsulot:
    
#     print(val["nom"],'va',val["narx"],"so'm",val["sana"]) 
#################################################################################################################################################


# mahsulotlar=[]
# bor=[{"nom":"non","narx":3000},{"nom":"olma","narx":10000},{"nom":"gruch","narx":25000},{"nom":"go'sht","narx":100000}]

# while True:
#     a=input("nima istaysiz\t")
#     mahsulotlar.append(a)
#     res=input("siz yana mahsulot olasizmi(ha/yoq)>>>")
#     if res=="ha":
#         continue
#     else:
#         break

# print("sizning mahsulotlaringiz")  

# t=False

# for m in mahsulotlar:
   
#    for b in bor :
       
#        if b["nom"]==m:
#            t=True
#            print(b["narx"],"sum")
    
    
# if (t==False):
#     print("bu mahsulo yoq")



###############################################################################################################################################

mahsulot=[]
market={"non":3000,"olma":10000,"anor":2000,"nok":30000}

while True:
    nom  = input ("nima kerak \t")
    mahsulot.append(nom)
    y=input("yana nimadur kerakmi:ha/yoq\t")
    if y == "ha":
        continue
    else:
        break


for val in mahsulot:
    if val in market.keys():
        print(val,":",market[val])    
  