'''
Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing', add 'ly' instead.
If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''

# my solution
def add_string(str):
    if len(str) < 3:
        return str
    elif len(str)>=3 and str.endswith("ing"):
        str+="ly"
    elif len(str)>=3 and not(str.endswith("ing")):
        str+="ing"
    return str


print(add_string("abc"))
print(add_string("abcing"))
print(add_string("string"))
print(add_string("ab"))