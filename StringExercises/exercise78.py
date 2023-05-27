'''
Write a Python program to count the number of non-empty substrings of a given string.
input : xbcefg
output : 2
'''

# w3resource solution
def count_char_position(str1):
    count=0
    for i in range(0,len(str1)):
        if (i==(ord(str1[i])-ord('a')) or i==(ord(str1[i])-ord('A'))):
            count+=1
    return count

print(count_char_position("xbcefg"))

