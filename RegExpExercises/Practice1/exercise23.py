'''
Write a Python program to replace whitespaces with an underscore and vice versa.
'''
# my solution
import re

text = 'Python Exercises'
text1=re.sub(r'\s',"_",text)
print(text1)
text2=re.sub(r'_'," ",text1)
print(text2)