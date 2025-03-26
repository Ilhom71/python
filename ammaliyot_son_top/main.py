import random

def bot_numbers():
    s=0
    u1=0
    n=random.randint(1,10)
    
    print("men 1 dan 10gach son o'yladim   top ishga urnib ko'rin")
    while n!=s:
   
     s=int(input("son yoz:"))
     u1+=1
     if n>s:
        print("men o'ylagan son katta")
        continue
     elif n<s:
        print("men o'ylagan son kichik")
        continue
     else:
        print(f"siz topdingiz !!!! \n siz {u1}ta urinishda topdingiz\n")
        return u1
        break         



def people_number():
    print("siz endi son o'ylan 1 dan 10 gacha  men topaman :" )
    sonlar=list(range(1,11))
    u2=0
    j=input("son o'ylagan bo'lsangiz istalgan tugmachani bosin !!!!")

    if j:
     while True:
        n=random.choice(sonlar)
        u2+=1
        print("siz o'ylaga son :",n)
        jav=str(input("to'gri bo'lsa (T),kichik bo'lsa (-),katta bo'lsa (+)"))
        if jav=='-':
            sonlar=sonlar[:n]
            
        elif jav=="+":
            sonlar=sonlar[n:]
           
        elif jav.title()=="T":
            print("men urinishlarim soni ",u2,"\n")
            return u2
            break;
            
            
while True:
    u1=bot_numbers()
    u2=people_number()
    if u1>u2:
        print("men yutdim menning urinishlar sonim 🤖",u2)
    elif u2>u1:
        print("siz yutdingiz siznig urinshlaringiz 🥳",u1)
        
    else :
        print("durang 🟰",u1,"=",u2)  
    
    t=input("yana o'ynaymizmi (HA/YOQ) :")
    
    if t.upper()=="HA":
        u1=0
        u2=0
        continue 
    elif t.upper()=="YOQ":
        break
    else:
        print("xato")  
        break                   
     
    


        

