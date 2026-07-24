# Function:
    # Reusable block of Code to Perform Specific Task

# 1.function definition/declaration 
# 2.function calling

# Syntax:
# *******
# Function Declaration
# def funcname():
#     #statement

# function Calling
# funcname()


def greet():
    print("Welcome to Python Function")

greet() # argument


# 1. arguments => actual Value
# 2. parameters => Alias name in Function declaration

def greet(name):
    print(f"Hi {name}! Welcome")

nam="vanuja"
greet(nam)
greet("suji")
greet("lingam")


def add(x,y):
    print(x+y)

a=5
b=10
add(a,b) # 15
add(a,b,20) #  TypeError: add() takes 2 positional arguments but 3 were given

# arguments counts needs to be match with Parameters 

# Arguments Types:
# 1. Positional Argument 
# 2. Named Argument
# 3. arbituary argument 
# 4. keyword argument
# 5. Default arguments

def add(a,b):
    print(a,b)

add(7,b=5)


def sample(a,b,c=0):
    print(a,b,c)
sample(10,20)
sample(10,20,30)


def sample(a,b,/,*,c):
    print(a,b,c)
# sample(10,20)
sample(10,20,c=30)


def sample(a,*b):
    print(a)
    print(b)

sample(1,2,3,4,5,6)


def sample(a,**b):
    print(a)
    print(b)
sample(a=10,b=20,c=30,d=40,e=50)

# Types:
1. buit-in
2. user-defined 
3. lambda 
4. recursion 


# 1. built-in function
# print()
# len()
# count() 

# 2.User defined Function 
# Type:
# 1. without argument without return
# 2. without argument with return 
# 3. with argument without return 
# 4. with argument with return


# type 1: without argument without return


def greet():
    print("Welcome")

greet()

def add():
    a=10
    b=20
    print(a+b)
add()


# type 2: without argument with return 
def mul():
    a=20
    b=3
    c=a*b 
    return c

print(mul())
z=mul()
print(z)

def mul():
    a=20
    b=3
    print("I am in Function")
    return (a*b) 
print(mul())
z=mul()
print(z)

# Type 3. with argument without return 

def userlogin(uname,password):
    if uname=="Vanu" and password == "vanu@123" :
        print("Valid Credentials")
    else:
        print("invalid Credentails")

name="Vanu"
pwd="vanu@123"
userlogin(name,pwd)
print(userlogin(name,pwd))

# Type 4. with argument with return 

def calculate(a,b,c):
    # print(a,b,c) 
    if c == "add":
        return(a+b)
    elif c== "sub":
        return(a-b)
    elif c== "mul":
        return (a*b)
    else:
        return(a/b)

print(calculate(10,20,"add"))
print(calculate(10,20,"sub"))
# Type 4. with argument with return 

def calculate(a,b,c):
    # print(a,b,c) 
    if c == "add":
        return(a+b)
    elif c== "sub":
        return(a-b)
    elif c== "mul":
        return (a*b)
    else:
        return(a/b)

print(calculate(10,20,"add"))
print(calculate(10,20,"sub"))

def calculate(a,b,c):
    # print(a,b,c) 
    if c == "add":
        d=a+b
    elif c== "sub":
        d=a-b
    elif c== "mul":
        d=a*b
    else:
        d=a/b
    return d
print(calculate(10,20,"mul"))
print(calculate(50,2,"div"))


# lambda:
# Anonymous Function 
# single line Expression
# accept multiple parameter but return single Expression    

z=lambda a,b,c: print(a+b+c)
z(10,20,30)