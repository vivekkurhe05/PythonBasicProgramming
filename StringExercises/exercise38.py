'''
Write a Python program to count occurrences of a substring in a string.
'''

# my solution
def count_occurrences(input):
    string = "The quick brown foxes jumps over the lazy dog"
    return string.count(input)
print(count_occurrences("fox"))