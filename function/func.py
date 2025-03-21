# name=str(input("ismmin yoz :"))
# age=int(input("yoshin yoz :"))


# def year(n="foydalanuvchi",a=0):
#     print(f"salom {n} siz {2025-a}-yilda tug'ilgan siz")


# year(name,age)    
#######################################################################################################

# num=int(input("son yoz men unin kvadratni va kubni aytaman :"))

# def level(n=0):
#     print(f"bu kvadrati:{n**2}\nbu kubi :{n**3} ")
    
# level(num)    

##########################################################################################################

# num = int(input("son yoz :"))

# def f(n=0):
#     if n%2==0:
#         print("son juft")
#     else:
#         print("bu toq")
            
            
            
# f(num)            

#######################################################################################################


# num1=int(input("son1 yoz :"))
# num2=int(input("son2 yoz :"))

# def bign(n1=0,n2=0):
#     if n1>n2:
#         print(n1,'-katta')
#     elif n2>n1:
#         print(n2,"-katta")
#     else:
#         print("teng")
        
# bign(num1,num2)            
            
            
######################################################################################################


# x=int(input("son yoz :"))
# y=int(input("son qaysi darajsi kerak :"))


# def level(n=0,m=0):
#     print(n**m)
                
                
# level(x,y)                


#########################################################################################################


# x=int(input("son yoz :"))
# y=int(input("son qaysi darajsi kerak :"))


# def level(n=0,m=2):
#     print(n**m)
                
                
# level(x,y)  


############################################################################################################


num = int(input("son yoz :"))



def nm(n):
    
    print("bo'linish alomatlari ",n)
    #for val in range (2,11):
    for val in range (2,n):
        if n % val==0:
            print(val,"bu son qoldiqsiz bo'linadi")
    


nm(num)