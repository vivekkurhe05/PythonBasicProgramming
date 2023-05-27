'''
Write a Python program to delete all occurrences of a specified character in a given string.
Sample Output:
Original string:
Delete all occurrences of a specified character in a given string
Modified string:
Delete ll occurrences of specified chrcter in given string
'''

# my solution
def delete_all_occurrences(str1):
    new_str=""
    for chr in str1:
        if chr == 'a':
            continue
        new_str+=chr
    return new_str
print(delete_all_occurrences("Delete all occurrences of a specified character in a given string"))