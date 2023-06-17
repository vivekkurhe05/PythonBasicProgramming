'''
Write a Python program that matches a string that has an a followed by zero or one 'b'.
'''
# my solution
import re
def text_match(str1):
    matchObj=re.search(r'^ab?$', str1)
    return bool(matchObj)
print(text_match("ab"))
print(text_match("abc"))
print(text_match("abbc"))
print(text_match("aabbc"))