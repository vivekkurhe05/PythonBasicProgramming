'''
Write a Python program to check for a number at the end of a string.
'''
# my solution
import re
def end_num(str1):
    matchObj=re.search(r'^\w+\d$',str1)
    return bool(matchObj)
print(end_num('abcdef'))
print(end_num('abcdef6'))