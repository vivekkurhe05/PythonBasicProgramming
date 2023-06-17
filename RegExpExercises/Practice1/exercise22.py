'''
Write a Python program to find the occurrence and position of substrings within a string.
'''
import re

text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

matches=re.finditer(pattern,text)
for match in matches:
    start_index=match.start()
    end_index=match.end()
    print('Found exercises at',str(start_index)+":"+str(end_index))

