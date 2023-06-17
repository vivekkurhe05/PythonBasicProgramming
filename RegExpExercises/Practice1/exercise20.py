'''
Write a Python program to search for a literal string in a string and also find the
location within the original string where the pattern occurs
'''
# my solution
import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
matchObj=re.search(pattern,text)
print(matchObj.start())