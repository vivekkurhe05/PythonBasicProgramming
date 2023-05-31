'''
Write a Python program to create a new JSON file from an existing JSON file.
'''
#my solution

try:
    file1=open("test.json","r")
    file2 = open("testnew.json", "w")
    data = file1.read()
    file2.write(data)
    file1.close()
    file2.close()
    print("Data copied successfully")
except:
    print("File does not exist")

