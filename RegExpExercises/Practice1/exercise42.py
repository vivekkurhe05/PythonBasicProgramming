'''
Write a Python program to find URLs in a string.
'''
# my solution
import re

text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
urls=re.finditer(r'http[s]?://\w+\.[a-z]{3}', text)
for url in urls:
    print(url.group())