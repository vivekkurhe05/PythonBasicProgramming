'''
Write a Python program that matches a string that has an a followed by two to three 'b'.
'''
# my solution
import re
def text_match(text):
    matchObj=re.search(r'ab{2,3}',text)
    return bool(matchObj)
print(text_match("ab"))
print(text_match("aabbbbbc"))