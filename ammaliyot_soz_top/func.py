from sozlar import uzbek_sozlar as s
import random




def key(arr,k="",j=""):
    
    soz=""
    if k:
       a=[]
       for val in arr:
           if val == j:
               a.append(j)
           else:
               a.append("-")
        
       txt = list(k)
       u=len(arr)
       for val in list(range(u)):
           if txt[val]=="-":
               txt[val]=a[val]
               soz+=txt[val]
           else:
               soz+=txt[val]    
                  
             
           
    else:
      for val in arr:
         if val == j:
            soz+=j    
         else:
            soz+="-"    
    return soz               
            

def soz(arr=s):
    ran_soz=random.choice(arr)
    return ran_soz


def sorov(random_soz):
    arr=list(random_soz)
    
    ke=key(arr)
    k=ke
    
    urinshlar=""
    son=0
    print("men so'z o'ylayman topishga harakat qilib korin :",arr)
    
    while True :
        
        print(k)
        j=input("harif yoz :")
        urinshlar+=j
        son+=1
        print("urinishlar :",urinshlar)
        for v in arr :
            if v==j:
                ke=key(arr,k,j)
                k=ke
            
        
        if random_soz.find(j)+1:
            print('bor')
        else:
            print("yoq")      
        
        if k.lower() == random_soz.lower():
            print(f"tabriklaymiz siz yutdingiz 🥳 men o'ylagan so'z bu {random_soz} edi siz {son} mart urinib topdingiz" )
            break         
        
                
        
        
     
        
                  
        
   
    
    

  
         



                
        
    


        
    