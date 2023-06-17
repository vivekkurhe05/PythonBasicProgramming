'''
Write a Python program to split a string into uppercase letters.
'''
# my solution
import re

text = "PythonTutorialAndExercises"
li=re.split(r'(?=\B[A-Z])', text)
print(li)