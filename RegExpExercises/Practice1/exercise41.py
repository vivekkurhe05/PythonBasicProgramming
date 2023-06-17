'''
Write a Python program to remove everything except alphanumeric characters from a string.
'''
# my solution
import re

text1 = '**//Python Exercises// - 12. '
text2=re.sub(r'[^a-zA-Z0-9]', "", text1)
print(text2)