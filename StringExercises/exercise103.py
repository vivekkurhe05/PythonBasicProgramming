'''
Write a Python program to replace each character of a word of length five and more with a hash character (#).
Sample Output:
Original string: Count the lowercase letters in the said list of words:
Replace words (length five or more) with hash characters in the said string:
##### the ######### ####### in the said list of ######
Original string: Python - Remove punctuations from a string:
Replace words (length five or more) with hash characters in the said string:
###### - ###### ############ from a #######
'''

# my solution
def replace_with_hash(str1):
    li=str1.split(" ")
    str2=""
    for word in li:
        if len(word) >=5:
            spe="#" * 5
            str2+=spe+" "
        else:
            str2+=word+" "
    return str2
print(replace_with_hash("Count the lowercase letters in the said list of words:"))
print(replace_with_hash("Python - Remove punctuations from a string:"))