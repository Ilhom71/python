text=["katta","kichik","o'rta","yuqqori"]
###########################################
# def up(t):
#     a=[]
    
#     for val in t:
        
#        a.append(val.capitalize())
      
#     return a    

# a=up(text)
# print(a)
###########################################

def name(n):
    b={}
    while n:
        a=n.pop()
        yoz=input(f"{a} baho berin \t")
        b[a]=yoz
    return b    


a=name(text)
print(a)        