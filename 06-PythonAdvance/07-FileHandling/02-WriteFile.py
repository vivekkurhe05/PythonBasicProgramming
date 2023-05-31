# Writing data to the file
obj = open("Py2.txt", "w")
obj.write("Hello this is new data")
print("Data written successfully")
obj.close()

# Appending data to the existing file
obj=open("Py2.txt","a")
obj.write("This is appending text")
print("Data appended successfully")
obj.close()

# with open(filename) as fileobject - with statement closes the file for you without you telling it to.