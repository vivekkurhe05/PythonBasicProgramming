'''
We can create an object of File class by calling predefined open method
We need to open file by setting opening mode
r - read mode, w - write mode, a - append mode, r+ - read & write mode, w+ - write & read mode,
a+ - append & read mode
'''

# Reading data from the file

obj = open("Py1.txt", "r")

# Read all data from the file
# print(obj.read())

# Read 1 line from the file
# print(obj.readline())

# Read only few characters from the file
# print(obj.read(10))

# Read all characters from file and display 1 by 1
# for i in obj.read():
#     print(i)

# Read all data from file line by line
s=obj.readline()
# loop while s exists
while s:
    print(s)
    s = obj.readline()