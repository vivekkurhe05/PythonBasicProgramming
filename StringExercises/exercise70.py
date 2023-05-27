'''
Write a Python program that concatenates uncommon characters from two strings.
'''

# my solution
def uncommon_chars_concat(str1, str2):
    uniq_str=""
    for chr in str1:
        if not(chr in str2):
            uniq_str+=chr
    for chr in str2:
        if not(chr in str1):
            uniq_str+=chr
    return uniq_str

print(uncommon_chars_concat("abcdpqr","xyzabcd"))