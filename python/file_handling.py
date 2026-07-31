# mode 
# 1. read = 'r'
# 2. append = 'a' append with exsiting Content
# 3. write = 'w' -> Replace with new



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
# 1. read() --> Read full file
# 2. readline() --> Read first line only
# 3. readlines() --> Read all and convert into list

file=open("suji.txt",'r')
print(file.read())
file.close()


with open("suji.txt",'r') as file:
    print(file.readline())

with open("suji.txt",'r') as f:
    print(f.readlines())
