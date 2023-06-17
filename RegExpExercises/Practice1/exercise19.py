'''
Write a Python program to search for literal strings within a string.
'''
# my solution
import re
patterns = [ 'fox', 'dog', 'horse' ]
text = 'The quick brown fox jumps over the lazy dog.'
for item in patterns:
    if re.search(item,text):
        print('Match is found')
    else:
        print('No match is found')