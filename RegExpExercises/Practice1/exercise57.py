'''
Write a Python program that checks whether a word starts and ends with a vowel in a given string.
Return true if a word matches the condition; otherwise, return false.
'''
# my solution
import re
def test(str1):
    match=re.search(r'\b[aeiouAEIOU]\w+[aeiouAEIOU]\b',str1)
    return bool(match)
print(test("Red Orange White"));
print(test("Red White Black"));
print(test("abcd dkise eosksu"));