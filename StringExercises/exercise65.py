'''
Write a Python program to find all the common characters in lexicographical order
from two given lower case strings. If there are no similar letters print "No common characters".
'''

# my solution
def common_chars(str1, str2):
    arr1=list(str1)
    arr2=list(str2)
    for el in arr1:
        if el in arr2:
            return el
    return "No common characters"

print(common_chars("Python","PHP"))
print(common_chars("Java", "PHP"))