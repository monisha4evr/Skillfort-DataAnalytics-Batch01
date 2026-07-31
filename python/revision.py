a="flower"
b="vegetabel"
print(f"String:{a} Vegi : {b}")
print("String",a,"Veg",b)

print(int("+1"))
print(int("1a"))

a=10
b=10
print(a is b)

a=[1,2,3]
b=[1,2,3]
print(a is b)

a=(1,2,3)
b=(1,2,3)
print(a is b)

a={1}
print(type(a))

a=(1,)
print(type(a))


a=10
b=20
a,b=b,a
print(a,b)

temp=a
a=b
b=temp 
print(a,b)


print(list(range(1,5)))


print("Even" if 5%2==0 else "Odd")

print([x for x in range(10) if x%2==0])

file=open("lingam.txt",'')