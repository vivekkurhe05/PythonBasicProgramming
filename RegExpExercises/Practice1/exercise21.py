'''
Write a Python program to find the substrings within a string.
Sample text:
'Python exercises, PHP exercises, C# exercises'
Pattern:
'exercises'

Note: There are two instances of exercises in the input string.
'''
# my solution
import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
li=re.findall(pattern,text)
for item in li:
    print('Found',item)