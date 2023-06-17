'''
Write a Python program to remove words from a string of length between 1 and a given number.
'''
# my solution
import re
def remove_words(text,num):
    return re.sub(r'\b\w{1,'+str(num)+'}\\b',"",text)
text = "The quick brown fox jumps over the lazy dog."
print(remove_words(text, 4))