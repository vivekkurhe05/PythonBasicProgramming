'''
Write a Python program to decapitalize the first letter of a given string.
Sample Output:
java Script
python
'''

def decapitalize_first_letter(str1):
    return str1[0].lower()+str1[1:]
print(decapitalize_first_letter("Java Script"))
print(decapitalize_first_letter("Python"))