'''
Write a Python program to remove lowercase substrings from a given string.
'''
# my solution
import re
str1 = 'KDeoALOklOOHserfLoAJSIskdsf'
text=re.sub(r'[a-z]+',"",str1)
print(text)