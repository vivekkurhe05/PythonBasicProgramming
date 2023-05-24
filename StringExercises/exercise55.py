'''
Write a Python program to find the first repeated word in a given string.
'''

# noted
# my solution
def first_repeated_word(str1):
    li = str1.split(" ")
    counts = {}
    for word in li:
        if word in counts:
            return word
        counts[word]=1
print(first_repeated_word("ab ca bc ab")) # ab
print(first_repeated_word("ab ca bc ab ca ab bc")) # ab
print(first_repeated_word("ab ca bc ca ab bc")) # ca
print(first_repeated_word("ab ca bc")) # None