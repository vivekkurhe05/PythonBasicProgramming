'''
Write a Python program to remove the parenthesis area in a string.
'''
# my solution
import re
items = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for item in items:
    text=re.sub(r'\(.+\)',"",item)
    print(text)