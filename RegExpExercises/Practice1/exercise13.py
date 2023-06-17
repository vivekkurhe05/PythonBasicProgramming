'''
Write a Python program that matches a word containing 'z', not the start or end of the word.
'''
# my solution
import re
def text_match(str1):
    matchObj=re.search(r'\w*\Bz\B\w*',str1)
    return bool(matchObj)
print(text_match("The quick brown fox jumps over the lazy dog.")) # True
print(text_match("Python Exercises.")) # False