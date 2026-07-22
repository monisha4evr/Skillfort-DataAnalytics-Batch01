a=100
b=20
c=15

if a>b and a>c:
    print(" a is Bigger ")
elif b>c:
    print("B is Bigger")
else:
    print("C is Bigger")

a=51
print("Even" if a%2==0 else "Odd")

# String

a="Flower"
print(a[3])

# Slicing
#[start:end:step]

b="I am learning Python"
print(b[2:4])
print(b[:5])
print(b[5:10])
print(b[::2])
print(b[::-1])


c=" flowers "
print(c[1:4])
print(c.capitalize())
print(len(c))
print(c.find('l'))
print(c.index('l'))
print(c)
print(c.strip())

strng="madamss"
#city
rev=strng[::-1]
print(strng)
print(rev)
if strng == rev:
    print("Palindrome")
else:
    print("not a Palindrome")


a="Hello "*5
print(a)


a=["f","l","o","w","e","r"]
print(''.join(a))

a="i am Learning python"
print(a.split(' '))
