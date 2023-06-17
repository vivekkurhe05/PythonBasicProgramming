'''
Write a Python program to match if two words from a list of words start with the letter 'P'.
'''
# my solution
import re

matches=[]
words = ["Python PHP", "Java JavaScript", "c c++"]
for item in words:
    if re.search(r'P\w+', item):
        matches.append(item)

print(matches)