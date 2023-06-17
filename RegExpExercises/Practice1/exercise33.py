'''
Write a Python program to find all five-character words in a string.
'''
# my solution
import re

text = 'The quick brown fox jumps over the lazy dog.'

li=re.finditer(r'\b[a-zA-Z]{5}\b',text)
for item in li:
    print(item.group())