'''
Write a Python program to find the maximum length of consecutive 0's in a given binary string.
str1 = '111000010000110'
str1 = '111000111'
'''

# noted
# my solution
def myFunc(e):
    return len(e)
def max_consecutive_0(str1):
    li = str1.split("1")
    new_li=[]
    for el in li:
        if el == "":
            pass
        else:
            new_li.append(el)

    new_li.sort(reverse=True, key=myFunc)
    return new_li[0]
print(max_consecutive_0("111000010000110"))
print(max_consecutive_0("111000111"))
