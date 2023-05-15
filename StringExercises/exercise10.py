'''
Write a Python program to change a given string to a newly
string where the first and last chars have been exchanged.
Sample String : abcd
Expected Result : dbca
'''

# my solution
def change_string(string):
    first_char=string[0]
    last_char=string[-1]
    return last_char+string[1:-1]+first_char
print(change_string("abcd"))