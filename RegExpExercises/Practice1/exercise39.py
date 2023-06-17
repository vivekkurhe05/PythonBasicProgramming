'''
Write a Python program to remove multiple spaces from a string.
'''
# my solution
import re

text1 = 'Python      Exercises'
text2=re.sub(r'\s+',' ', text1)
print(text2)