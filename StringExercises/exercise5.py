'''
Write a Python program to get a single string from two given strings, separated by a space
and swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
'''

# my solution
def swapLetters(str1,str2):
    newStr1 = str2[0:2] + str1[len(str1)-1]
    newStr2 = str1[0:2] + str2[len(str2)-1]
    return newStr1 + " " + newStr2

print(swapLetters("abc","xyz"))