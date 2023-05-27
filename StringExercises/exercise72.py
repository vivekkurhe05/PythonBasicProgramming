'''
Write a Python program to remove all characters except a specified character from a given string.
Original string
Python Exercises
Remove all characters except P in the said string:
P
Original string
google
Remove all characters except g in the said string:
gg
Original string
exercises
Remove all characters except e in the said string:
eee
'''

# my solution
def remove_all_chars_except(str1, char):
    new_str=""
    for chr in str1:
        if chr == char:
            new_str+=chr
    return new_str
print(remove_all_chars_except("Python Exercises","P"))
print(remove_all_chars_except("google","g"))
print(remove_all_chars_except("exercises","e"))
