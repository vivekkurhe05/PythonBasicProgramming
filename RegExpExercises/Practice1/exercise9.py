'''
Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.
'''
# my solution
import re
def text_match(text):
    matchObj=re.search(r'^a.+b$',text)
    return bool(matchObj)
print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))