'''
Write a Python program to remove all whitespaces from a string.
'''
# my solution
import re

text1 = ' Python    Exercises '
text2=re.sub(r'\s+',"",text1)
print(text2)