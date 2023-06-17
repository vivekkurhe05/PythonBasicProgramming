'''
Write a Python program that matches a string that has an a followed by zero or more b's.
'''
# my solution
import re
def text_match(str1):
    matchObj=re.search(r'^ab*$', str1)
    return bool(matchObj)
print(text_match("ac")) # False
print(text_match("abc")) # False
print(text_match("a")) # True
print(text_match("ab")) # True
print(text_match("abb")) # True