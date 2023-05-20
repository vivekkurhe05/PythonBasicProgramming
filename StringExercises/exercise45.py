'''
Write a Python program to check whether a string contains all letters of the alphabet.
'''

# my solution
def all_alphabets(string):
    string=string.lower().replace(' ','')
    alphabets="abcdefghijklmnopqrstuvwxyz"
    li=[]
    flag=False
    for i in alphabets:
        if i in string:
            li.append(True)
        else:
            li.append(False)
    for i in li:
        if i==True: flag=True
        else:
            flag= False
            break
    return flag
print(all_alphabets("The quick brown fox jumps over the lazy dog"))
print(all_alphabets("The quick brown fox jumps over the lazy cat"))

# or my solution using __Contains__()

def all_alphabets2(string):
    string=string.lower().replace(' ','')
    alphabets="abcdefghijklmnopqrstuvwxyz"
    li=[]
    flag=False
    for i in alphabets:
        if string.__contains__(i):
            li.append(True)
        else:
            li.append(False)
    for i in li:
        if i==True: flag=True
        else:
            flag= False
            break
    return flag
print(all_alphabets2("The quick brown fox jumps over the lazy dog"))
print(all_alphabets2("The quick brown fox jumps over the lazy cat"))