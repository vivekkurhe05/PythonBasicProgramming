'''
Write a Python program to make two given strings (lower case, may or may not be of the same length)
anagrams without removing any characters from any of the strings.
'''

# my solution
def make_anagram(str1,str2):
    arr1=list(str1)
    arr2=list(str2)
    li=[]
    for el in arr1:
        if not(el in arr2):
            li.append(el)
    for el in arr2:
        if not(el in arr1):
            li.append((el))
    return len(li)
print(make_anagram("The quick brown fox", "jumps over the lazy dog"))