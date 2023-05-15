'''
Write a Python function that takes a list of words and return the longest word and
the length of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9
'''

# my solution
def longest_word(li):
    word_len = len(li[0])
    for i in range(0,len(li)):
        try:
            if (word_len < len(li[i+1])):
                longest_word = li[i+1]
                word_len = len(longest_word)
        except:
            return longest_word

print(longest_word(["PHP","Exercises","Backend"]))