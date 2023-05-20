'''
Write a Python program to print the index of a character in a string.
Sample string: w3resource
Expected output:
Current character w position at 0
Current character 3 position at 1
Current character r position at 2
- - - - - - - - - - - - - - - - - - - - - - - - -
Current character c position at 8
Current character e position at 9
'''

# my solution
str1='w3resource'
for i in range(0,len(str1)):
    print('Current character '+str1[i]+' position at '+str(i))