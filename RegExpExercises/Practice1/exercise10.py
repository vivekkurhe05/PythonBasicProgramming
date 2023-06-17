'''
Write a Python program that matches a word at the beginning of a string.
'''
# my solution
import re
def text_match(text):
    matchObj=re.search(r'^\w+',text)
    return bool(matchObj)
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" The quick brown fox jumps over the lazy dog."))