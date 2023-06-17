'''
Write a Python program to convert snake-case string to CamelCase string.
'''
# my solution
import re
def snake_to_camel(text):
    li=re.split("_", text)
    str1=li[0]
    str2=li[1]
    return str1[0].upper()+str1[1:]+str2[0].upper()+str2[1:]
print(snake_to_camel('python_exercises'))