'''
Write a Python program to find the first repeated character in a given string.
'''

# noted
# my solution
def first_repeating_character(str1):
    counts={}
    for chr in str1:
        if chr in counts:
            return chr
        counts[chr]=1
print(first_repeating_character('abcdabcd'))
print(first_repeating_character('abcd'))
print(first_repeating_character('abcdee'))