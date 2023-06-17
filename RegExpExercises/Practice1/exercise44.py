'''
Write a Python program to do case-insensitive string replacement.
'''
import re

text = "PHP Exercises"
text2=re.search(r'\b[A-Z]+\b', text)
print(text2.group().lower())