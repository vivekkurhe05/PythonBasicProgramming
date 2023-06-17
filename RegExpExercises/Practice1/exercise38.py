'''
Write a Python program to extract values between quotation marks of a string.
'''
# my solution
import re

text1 = '"Python", "PHP", "Java"'
li=re.finditer(r'\w+',text1)
for item in li:
    print(item.group())