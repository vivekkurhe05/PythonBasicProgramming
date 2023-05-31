'''
Write a Python program to append text to a file and display the text.
'''

with open("abc.txt","a") as file:
    file.write("\nJavascript")
with open("abc.txt") as file:
    print(file.read())