'''
Write a Python program to find all adverbs and their positions in a given sentence.
'''
# my solution
import re
text = "Clearly, he has no excuse for such behavior."
matches = re.finditer(r'[a-zA-Z]+ly\b',text)
for match in matches:
    print(match.group())