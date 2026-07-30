# oops=> object Oriented Program

# class : Blue print
# object : instance of class 

# in Class
# variable : (attribute)
# function(method)

# Constructor 
# its Called Automatically while object is created
# keyword: __init__
# variable Initialize

# destructor:
# __del__()

# class Classname:
#     def methodname():
#         pass 

# methods type:
# 1. instance self
# 2. classmethod  cls
# 3. staticmethod


class Fruits:
    def display(self):
        print("I am a Fruit")

fruit =Fruits()
fruit.display()

class Bird:
    def display(self,name):
        print(name)


b=Bird()
b.display("cuckoo")

class Vegetables:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def display(self):
        print(f"Vegetable name:{self.name}  Color: {self.color}")

vegi=Vegetables("Carrot","orange")
vegi.display()


# classmethod:

class Animals:
    animal1="dog"
    animal2="cat"
    animal3="cow"

    @classmethod
    def display(cls):
        print(f" Animal 1: {cls.animal1}  Animal 2: {cls.animal2} Animal 3: {cls.animal3}") 

a=Animals()
a.display()
Animals.display()

# static Method
class Student:
    @staticmethod
    def display(name):
        print("Welcome",name)

s=Student()
s.display("Suji")

# pillar of Oops:

# 1. inheritance 
# 2. Polymorphism
# 3. Encapsulation
# 4. Abstraction

# inheritance:
# -------------

# 1. single inheritance
# 2. multiple inheritance
# 3. multilevel inheritance
# 4. hierarchial inheritance

# single inheritance :

class Parent:
    def parent_display(self):
        print("I am Parent")

class Child(Parent):
    def child_display(self):
        print("I am Child")

c=Child()
c.parent_display()
c.child_display()

#multiple inheritance:
class Parent:
    def parent_display(self):
        print("I am Parent")

class Mother:
    def display(self):
        print("I am mother")     

class Child(Parent,Mother):
    def child_display(self):
        print("I am Child")

c=Child()
c.parent_display()
c.child_display()
c.display()

# multilevel inheritance:

class Parent:
    def parent_display(self):
        print("I am Parent")

class Mother(Parent):
    def display(self):
        print("I am mother")     

class Child(Mother):
    def child_display(self):
        print("I am Child")

c=Child()
c.display()
c.parent_display()
c.child_display()

#hierarchical inheritance:

class Parent:
    def display(self):
        print("Parent")

class Child(Parent):
    def child_display(self):
        print("Child")

c=Child()
c.display()
c.child_display()

class Son(Parent):
    def son_display(self):
        print("son")

s=Son()
s.son_display()
s.display()


#Encapsulation
# Bind Data Eg:Class 
# Security 
# public 
# protected (_)
# private (__)
# NameMangling

class Userprofile:
    def __init__(self,username,mobile,password):
        self.username=username
        self._mobile=mobile
        self.__password=password 

    def get_pwd(self):
        print(self.__password)

    def set_pwd(self,newpassword):
        self.__password=newpassword


u=Userprofile("vanu",122334,"ad@123")
print(u.username)
print(u._mobile)
u.get_pwd()
u.set_pwd("vanu@123")
u.get_pwd()
print(u._Userprofile__password)

# polymorphism
# 1. Overloading 
# 2. Overriding


class Demo:
    def add(self,a,b,c=0,d=None,*e):
        print(e)
        if d:
            print(a+b+c+d)
        else:
            print(a+b+c)

d=Demo()
d.add(5,5)
d.add(5,5,1)
d.add(5,5,1,2)
d.add(5,5,1,2,4,6,7,8,7)

#overriding:
# parent and child class
# parent class method replaced by Child Class

class Animal:
    def sound(self):
        print("Animals make Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks.......")
d=Dog()
d.sound()

# using Super()
class Animal:
    def __init__(self):
        print("Animals make Sound")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Barks.......")
d=Dog()

# Abstraction
# hiding unnecessary implementation 
# showing Neccessary code 

from abc import ABC,abstractmethod
class Calculation(ABC):
    @abstractmethod
    def area(self):
        pass
    def display(self):
        print("Displayeed")

class Triangle(Calculation):
    def area(self):
        print("area")

    def display_triangle(self):
        print("I am triangle")

t=Triangle()
t.display_triangle()
t.area()


class Grandparent:
    def __init__(self):
        print("Grand Parent")

class Father(Grandparent):
    def __init__(self):
        super().__init__()
        print("Father")

class Mother(Grandparent):
    def __init__(self):
        super().__init__()
        print("Mother")

class Child(Grandparent):
    def __init__(self):
        super().__init__()
        print("I am child")

c=Child()
print(Child.__mro__)


class Grandparent:
    def __init__(self):
        print("Grand Parent")

class Father(Grandparent):
    def __init__(self):
        print("Father")

class Mother(Father):
    def __init__(self):
        print("Mother")

m=Mother()






