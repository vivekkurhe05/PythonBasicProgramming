'''
Write a Python program to check that a string contains only a
certain set of characters (in this case a-z, A-Z and 0-9).
'''
# my solution
import re

def is_allowed_specific_char(str1):
    matchObj=re.search(r'[a-zA-z0-9]',str1)
    return bool(matchObj)

print(is_allowed_specific_char("ABCDEFabcdef123450")) # True
print(is_allowed_specific_char("*&%@#!}{")) # False