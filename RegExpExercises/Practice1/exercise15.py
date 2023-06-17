'''
Write a Python program that starts each string with a specific number.
'''
# my solution
import re
def match_num(str1):
    matchObj=re.search(r'^5',str1)
    return bool(matchObj)
print(match_num('5-2345861')) # True
print(match_num('6-2345861')) # False