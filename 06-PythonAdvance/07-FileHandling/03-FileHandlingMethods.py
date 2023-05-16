# tell() - It tells you the current cursor position in a file
obj=open("Py1.txt","r")
print(obj.tell())
obj.readline()
print(obj.tell())
obj.readline()
print(obj.tell())

# seek() - It navigates cursor position to the different position
print(("Seek method"))
obj.seek(5) # it takes cursor to the 5th character
print(obj.tell())