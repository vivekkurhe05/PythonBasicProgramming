'''
Write a Python program to remove duplicate words from a given string.
Sample Output:
Original String:
Python Exercises Practice Solution Exercises
After removing duplicate words from the said string:
Python Exercises Practice Solution
'''

# my solution
def remove_duplicate_words(str1):
    li=str1.split(" ")
    str2=""
    for word in li:
        if word not in str2:
            str2+=word+" "
    return str2
print(remove_duplicate_words("Python Exercises Practice Solution Exercises"))
