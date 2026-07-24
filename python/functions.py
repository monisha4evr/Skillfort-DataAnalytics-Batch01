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
