'''
Write a Python program to match a string that contains only
upper and lowercase letters, numbers, and underscores.
'''
# my solution
import re
def text_match(str1):
    matchObj=re.search(r'^\w+$',str1)
    return bool(matchObj)
print(text_match("The quick brown fox jumps over the lazy dog.")) # False
print(text_match("Python_Exercises_1")) # True