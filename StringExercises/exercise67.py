'''
Write a Python program to remove all consecutive duplicates of a given string.
'''

# my solution
def remove_all_consecutives(str1):
    uniq_str=""
    for chr in str1:
        if not(chr in uniq_str):
            uniq_str+=chr
    return uniq_str
print(remove_all_consecutives("xxxxxyyyyy"))