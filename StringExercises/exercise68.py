'''
Write a Python program to generate two strings from a given string. For the first string,
use the characters that occur only once, and for the second,
use the characters that occur multiple times in the said string.
'''

# my solution 
def generate_strings(str1):
    di={}
    dup_str=""
    uni_str=""

    for chr in str1:
        count = 1
        if chr in di:
            dup_str+=chr
            count+=di[chr]
        di[chr]=count
    for chr in di:
        if di[chr] == 1:
            uni_str+=chr
    return uni_str, dup_str

print(generate_strings("aabbcceffgh"))