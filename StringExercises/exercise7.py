'''
Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'
Sample String : 'The lyrics is poor!'
Expected Result : 'The lyrics is poor!'
'''

# my solution
def not_poor(str):
    if(str.find("not that poor") != -1):
        str = str.replace("not that poor","good")
    return str


print(not_poor("The lyrics is not that poor!"))
print(not_poor("The lyrics is poor!"))