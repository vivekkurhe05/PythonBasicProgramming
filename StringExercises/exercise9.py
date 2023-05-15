'''
Write a Python program to remove the nth index character from a nonempty string.
'''

# my solution
def remove_char(word,index):
    newWord=''
    for i in range(0,len(word)):
        if i == index:
            continue
        else:
            newWord+=word[i]
    return newWord

print(remove_char("Python",3))

# or my solution

def remove_char(word,index):
    word1=word[:index]
    word2=word[index+1:]
    return word1+word2

print(remove_char("Python",4))