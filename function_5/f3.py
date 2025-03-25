def faktarila(n):
    if n==0:
        return 1
    return n*faktarila(n-1)

def fibbanachi(n):
    if n<=1:
        return n
    return fibbanachi(n-1)+fibbanachi(n-2)

def diskirminat(b,a,c):
    return (b**2)-(4*a*c)
    
    
        


def kvtenglama(a,b,c):
    l=diskirminat(b,a,c)
    
    if l>0:
        
      x1=(-b+(l**(1/2)))/(2*a)
      x2=(-b-(l**(1/2)))/(2*a)
      print()
      arr=[x1,x2]
      return arr
    elif l==0:
        x1=-b/(2*a)
    else:
       return 0

    
