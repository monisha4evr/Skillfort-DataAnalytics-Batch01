# 1. List

a=[1,2,3,4]
print(type(a))
print("**********")
a.append(5)
a.append([6,7])
print(a)
print("**********")
a.extend([6,7])
print(a)
a.insert(2,9)
print(a)


print("*******")
a=[5,10,15,20,25]
a.pop()
print(a)
a.pop(1)
print(a)

a.clear()
print(a)


a=[1,2,2,3,4,5,6,6,7,2,2]
print(a.count(9))


a=[1,2,3,4]
b=a
b.append(5)
print(a)

z=[5,6,7,8]
y=z.copy()
z.append(3)
print(y)

z=[1,2,3,4,5,6,7,8]
print(z.index(5)) # 4th position
print(z.index(9))


z=[1,2,3,4,5,6,7,8]
z.reverse()
print(z)

z=[1,4,7,2,9,3,1]
z.sort()
print(z)
z.sort(reverse=True)
print(z)

a=(1,2,3,5,2,4,4,4,44,4,4)
print(type(a))
print(a.count(4))
print(a.index(9))