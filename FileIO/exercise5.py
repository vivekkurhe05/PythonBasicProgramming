'''
Write a Python program to read a file line by line and store it into a list.
'''

with open("text.txt") as file:
    lines=file.readlines()
    print(lines)