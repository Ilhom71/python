# print("yaxshi ko'rgan kitoblarnigizni yozin")
# kitob=[]
# nom=''

# while nom!="stop":
#     nom=input("nom yoz yoki stop deb yoz\t")
#     kitob.append(nom)
# print(kitob)    
##################################################################################################################################################

# bl =True

# while bl:
#      b=input("yoshingizni yozin\t")
#      n=int(b) 
#      if(n<=7):
#         print("sizga 2000 so'm")
#      elif n>7 and n<=18 :
#         print("sizga 3000 so'm")
#      elif n>18 and n<=65:
#         print("sizga 10000 so'm")
#      elif n>65:
#         print("sizga bepul")

#      if str(b)=="stop" or str(b)=="quit":
#         b=False 
#      else:
#         b=tr   


# while True:
#     b=input("yoshni yoz\t")
    
#     if b.lower() =="stop":
#      print("stop bajarildi")
#      break   
        
#     n=int(b)
#     if(n<=7):
#        print("sizga 2000 so'm")
#     elif n>7 and n<=18 :
#        print("sizga 3000 so'm")
#     elif n>18 and n<=65:
#         print("sizga 10000 so'm")
#     elif n>65:
#         print("sizga bepul")
   
##################################################################################################################################################

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    
    
    
    if str(qiymat).capitalize()=='Exit':
        break
    elif int(qiymat)<=0:
        continue
    elif int(qiymat)>0:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    else:
        break    