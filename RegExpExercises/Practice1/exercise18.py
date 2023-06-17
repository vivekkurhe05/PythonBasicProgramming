'''
Write a Python program to search for numbers (0-9) of length between 1 and 3 in a given string.
'''
# my solution
import re
input = "Exercises number 1, 12, 13, and 345 are important"
li=re.findall(r'\d{1,}',input)
for item in li:
    print(item)