'''
Write a Python program to reverse words in a string.
'''

# my solution
def reverse_words(input):
    li=list(input)
    li.reverse()
    return "".join(li)

print(reverse_words("The quick brown fox"))