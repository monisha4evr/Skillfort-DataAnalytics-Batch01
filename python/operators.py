1. Arithmetic operator (+,-,*,/,%,**,//)
2. Assignment operator(+=,-=,*=,/=)
3. Comparision Operator (==,>,<.>=,<=,!=)
4. Logical Operator (and or not)
5. Bitwise Operator (&,|,~,^, >> , <<)
6. Membership Operator (in,not in)
7. Identity Operator (is, is not)


Arithmetic Operator:
---------------------

a=10
b=20
c=a+b
print(c)
print("Addition ",15+20)
print("Subtraction",155-20)
print("Multiplication ",15*20)
print("Division",21/2)
print("Floor Division",21//2)
print("Modulus", 21%2)
print("Exponential", 2**3)

2. Assigment Operator
----------------------

a=10
print(a)
a+=2
print(a)
a-=5
print(a)

3. Comparision
---------------

a=10
b=20
print(a>b)
print(10>20)
print(10<20)
a=35
b=40
print(a>=b)
a=30
b=30
print(a==b)

a=35
b=30
print(a!=b)

Logical Operator:

and 
True and False = False 
False and True = False
True and True = True 
false and false =False


or 

True or True = True 
True or False = True 
false or True = True 
false or false = False

not
true -> False
false -> true 

a=20 
b=30 
c=45
# print(a>b and b>c)
# print(a<b and b>c)
# print(20<30 and 20>10)

print(a>b or b>c)
print(a<b or b>c)
print(20<30 or 20>10)
print(40>10 or 30>10)

a=12
b=2
print(not a>b)

print(10 and 20)
print(30 or 0)

a=2  #0010
b=3  #0011
print(a&b)
print(a|b)

# 0010
# 0011
# -----
# 0011

a= 2 #=> 0000       10 
print(a>>2)
print(a<<2)
# 00    1000

# 6. Membership Operator 
# ----------------------

# in, not in

a=[1,2,3,4,5]

print( 3  in a)
print( 3 not in a)
print( 7  in a)
print( 7 not in a)


# 7. Identity Operator

# is, is not 

a=10
b=20 
print(id(a))
print(id(b))
print(a is b)

a=[1,2,3,4]
b=[1,2,3,4,5]
print(id(a))
print(id(b))
print(a is b)


a=(1,2,3,4)
b=(1,2,3,4)
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

