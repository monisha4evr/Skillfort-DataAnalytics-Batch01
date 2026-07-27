def add(a,b,c):
    print(a+b+c)

def sub(a,b):
    if a>b:
        c=a-b
    else:
        c=b-a 
    return c

def mul(a,b):
    return a*b 

def divi(a,b):
    if b:
        return a/b;
    else:
        return "b is 0"