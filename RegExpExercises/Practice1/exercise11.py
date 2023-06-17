'''
Write a Python program that matches a word at the end of a string, with optional punctuation
'''
# my solution
import re
def text_match(str1):
    matchObj=re.search(r'dog\.?$', str1)
    return bool(matchObj)
print(text_match("The quick brown fox jumps over the lazy dog.")) # True
print(text_match("The quick brown fox jumps over the lazy dog. ")) # False
print(text_match("The quick brown fox jumps over the lazy dog ")) # False