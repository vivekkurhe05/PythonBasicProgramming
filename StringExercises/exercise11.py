'''
Write a Python program to remove characters that have odd index values in a given string.
Sample String : abcdef
Expected Result : ace
Sample String : python
Expected Result : pto
'''

# my solution
def odd_values_string(string):
    new_string=''
    for i in range(0, len(string)):
        if not(i%2 == 0):
            pass
        else:
            new_string+=string[i]
    return new_string
print(odd_values_string("abcdef"))
print(odd_values_string("python"))