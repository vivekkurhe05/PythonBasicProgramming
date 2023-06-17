'''
Write a Python program to find the sequences of one upper case letter followed by lower case letters.
'''
# my solution
import re
def text_match(text):
    matchObj=re.search(r'^[A-Z]+[a-z]+$',text)
    return bool(matchObj)
print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))