'''
Write a Python program to find the common values that appear in two given strings.
Sample Output:
Original strings:
Python3
Python2.7
Intersection of two said String:
Python
'''

# my solution
def common_values(str1, str2):
    new_str=""
    for chr in str1:
        if chr in str2 and chr not in new_str:
            new_str+=chr
    return new_str
print(common_values("Python3", "Python2.7"))