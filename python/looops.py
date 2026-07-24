# Loops:
#     reduce the repitative Code
# 1. for loop
# 2. while loop

# Syntax: range(start,end,step)

# 0,1,2,3,4,5,6,7,8,9
print("Start")
for i in range(10):
    print(i)
print("End")

# 5,6,7,8,9,10
print("Loop Starts")
for i in range(5,11):
    print("I am in Loop")
    print(i)
print("Loop ended here....")

for i in range(1,11,2):
    print(i)

for i in range(6,11,2):
    print(i)

for i in range(10,0,-1):
    print(i)


a=[11,20,31,40,51,60]

for i in a:
    if i%2==0:
        print("Even")
    else:
        print(i)

print(list(range(1,6)))

a=1
while(a<=5):
    print(a)
    a+=1



a=1237
rev=0
while(a>0):
    r=a%10
    rev=rev*10+r
    a//=10

print(rev)

#Execution:
# a=123 ,rev=0 
# 123>0 T 
#     r=(123%10)=> 3
#     rev=0*10+3 => 3
#     a=12
# 12>0 True 
#     r (12%10)=> 2
#     rev = (3*10)+2 =>32 
#     a=(12//10) => 1

# 1>0 True 
#     r(1%10)=> 1 
#     rev=(32*10)+1  320+1 =321
#     a=0

# 0>0 False


#TASK

# 1
# 22
# 333
# 4444
# 55555

# 1
# 12
# 123
# 1234
# 12345

# *
# **
# ***
# ****
# *****

# reverse string without using ([::-1]) and find Palindrome


# 1
# 22
# 333
# 4444
# 55555

# 1
# 12
# 123
# 1234

# 1,2 3
for i in range(1,4):
    #1,2,3
    for j in range(i):
        print('*',end='')
    print()

a="hello"*5


# 1,2,3,4,5,
n=6
for i in range(n):
    print(" "*(n-i)+ "*"*i)


# enumerate

for i,j in enumerate(range(1,11,2)):
    print(i,j)


#Zip

a=[1,2,3]
b=[5,6,7]
for i,j in zip(a,b):
    print(i,j)

a=["Manoj","Jagadeesh","Sundar"]
b=['kumar',"M","lingam"]

for i,j in zip(a,b):
    print(i,j)


a=[1,2,3,4,5]

for i in a:
    if(i%2==0):
        print(i)

# List comprehension
a=[1,2,3,4,5]
print([i for i in a if i%2==0])
print([i*i for i in a if i%2!=0])

#dictionary comprehension
a=[1,2,3,4,5]
print({i for i in a if i%2==0})
print({i*i for i in a if i%2!=0})

#Task
# remove Duplicates in List [1,1,3,4,2,3,4,9,3]
# Anagram  Listen → Silent
# Fibonacci series 0 1 1 2 3 5 
# Factorial 5
# number Reverse without Built in  using for loop

a=str(531)
print(a[::-1])


# break // Exit from Loop
# continue // Skip the current Iteration
# pass // To skip Error

for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)