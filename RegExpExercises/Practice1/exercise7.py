'''
Write a Python program to find sequences of lowercase letters joined by an underscore.
'''
# my solution
import re
def text_match(text):
    matchObj=re.search(r'^[a-z]+_[a-z]+$',text)
    return bool(matchObj)
print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))