'''
Write a Python function to get a string made of the first three characters of a specified string.
If the length of the string is less than 3, return the original string.
Sample function and result :
first_three('ipy') -> ipy
first_three('python') -> pyt
'''

# my solution
def first_three(string):
    if(len(string)<3): return string
    return string[:3]
print(first_three("ipy"))
print(first_three("python"))