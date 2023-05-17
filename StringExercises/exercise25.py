'''
Write a Python program to create a Caesar encryption.

Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher,
Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter
some fixed number of positions down the alphabet. For example, with a left shift of 3,
D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar,
who used it in his private correspondence.
'''

# work on it
# it does not work as expected for a string xyz -> zab
def caesar_encrypt(string, shift):
    li=list(string)
    li2=[]
    newstring=""
    for i in range(0,len(li)):
        if li[i] == 'z':
            li2.append(ord(li[i]) -25)
        else:
            li2.append(ord(li[i]) + shift)

    for i in li2:
        newstring+=chr(i)
    return newstring
print(caesar_encrypt('abc', 2))