'''
Write a Python program that takes a string with some words. For two consecutive
words in the said string, check whether the first word ends with a vowel and the
next word begins with a vowel. If the program meets the condition,
return true, otherwise false. Only one space is allowed between the words.
'''
# my solution
import re
def test(str1):
    match=re.search(r'[AEIOUaeiou]\b\s[AEIOUaeiou]',str1)
    return bool(match)

print(test("These exercises can be used for practice."))
print(test("Following exercises should be removed for practice."))
print(test("I use these stories in my classroom."))