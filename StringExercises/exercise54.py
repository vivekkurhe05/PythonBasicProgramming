'''
Write a Python program to find the first repeated character in a
given string where the index of the first occurrence is smallest.
'''

# noted
# my solution
def first_repeated_char_smallest_index(str1):
    counts = {}
    for chr in str1:
        if chr in counts:
            index=str1.find(chr)
            return chr, index
        counts[chr]=1
print(first_repeated_char_smallest_index("abcabc")) # a, 0
print(first_repeated_char_smallest_index("abcb")) # b, 1
print(first_repeated_char_smallest_index("abcc")) # c, 2
print(first_repeated_char_smallest_index("abcxxy")) # x, 3
print(first_repeated_char_smallest_index("abc")) # None