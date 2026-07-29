# oops=> object Oriented Program

# class : Blue print
# object : instance of class 
# variable : (attribute)
# function(method)

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


