# mode 
# 1. read = 'r'
# 2. append = 'a'
# 3. write = 'w'



file=open("suji.txt",'w')
file.write("Welcome to File Handling")
file.close()


file=open("suji.txt",'w')
file.write("\nWelcome to Skillfort")
file.close()

file=open("suji.txt",'a')
file.write("\nLearning Python is Interesting")
file.close()



# read:
# 1. read()
# 2. readline()
# 3. readlines()

file=open("suji.txt",'r')
print(file.read())
file.close()


with open("suji.txt",'r') as file:
    print(file.readline())

with open("suji.txt",'r') as f:
    print(f.readlines())
