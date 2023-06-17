'''
Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.
'''
# my solution
import re
text = 'Python Exercises, PHP exercises.'
text1=re.sub(r'[\s,\.]+',":",text)
print(text1)