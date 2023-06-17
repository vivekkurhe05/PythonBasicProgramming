'''
Write a Python program to convert a camel-case string to a snake-case string.
'''
# my solution
import re
def camel_to_snake(text):
    li=re.split(r'(?=\B[A-Z])', text)
    return "-".join(li).lower()
print(camel_to_snake('PythonExercises'))