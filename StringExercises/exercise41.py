'''
Write a Python program to strip a set of characters from a string.
'''

# my solution
def strip_chars(input):
    chrs="aeiou"
    string=""
    for i in input:
        if(not(chrs.find(i)==-1)):
            pass
        else:
            string+=i
    return string
print(strip_chars("The quick brown fox jumps over the lazy dog"))