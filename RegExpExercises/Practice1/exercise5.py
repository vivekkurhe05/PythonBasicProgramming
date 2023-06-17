'''
Write a Python program that matches a string that has an a followed by three 'b'.
'''
# my solution
import re
def text_match(text):
    matchObj=re.search(r'ab{3}', text)
    return bool(matchObj)
print(text_match("abbb"))
print(text_match("aabbbbbc"))