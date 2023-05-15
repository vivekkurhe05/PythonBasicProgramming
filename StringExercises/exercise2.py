'''
Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
'''

# my solution
def count_characters(str):
    di = {}
    for i in range(0,len(str)):
        count=0
        index = str.find(str[i],0)
        while(index != -1):
            count+=1
            index=str.find(str[i],index+1)
            di[str[i]]=count
    return di
print(count_characters("google.com"))