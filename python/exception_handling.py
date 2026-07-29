# Error:
# 1. ValueError
# 2. TypeError
# 3. ZeroDivisionError


a=int("abc")
print(a)

b="1"+1
print(a)

c=10/0
print(c)



# 1. try
# 2. except
# 3. else 
# 4. finally 
# 5. raise - custom error


try:
    a=int("abc")
except ValueError:
    print("Cann't covert string to int")

try: 
    b="1"+1
    print(a)
except TypeError:
    print("cann't do this Operation")

try: 
    b="1"+1
    print(a)
except ValueError,TypeError:
    print("cann't do this Operation")

try:
    print(12/0)
except Exception as e:
    print(e)


try:
    print(10/0)

except Exception as e:
    print("Error:",e)

else:
    print("There is no Error in this Program")

finally:
    print("I always Run")


class AgeLimit(Exception):
    pass 
def checkAge(age):
    if age<0:
        raise AgeLimit("Age mustnot be Below Zero")
    else:
        print(f"your age is : {age}")

try:
    checkAge(-2)
except AgeLimit as error:
    print(error)



try:
    print(10/0)
except ValueError:
    print("value error")
except TypeError:
    print("Type Error")
except ZeroDivisionError :
    print("b is Zero")
except Exception as e:
    print("0")