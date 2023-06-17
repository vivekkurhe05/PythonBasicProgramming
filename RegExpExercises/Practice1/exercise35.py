'''
Write a Python program to find all words that are at least 4 characters long in a string.
'''
# my solution
import re

text = 'The quick brown fox jumps over the lazy dog.'
li=re.finditer(r'\b[a-zA-Z]{4,}\b',text)
for item in li:
    print(item.group())