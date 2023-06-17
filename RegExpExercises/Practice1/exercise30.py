'''
Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
'''
# my solution
import re

street = '21 Ramkrishna Road'
text=re.sub("Road","Rd.",street)
print(text)