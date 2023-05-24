'''
Write a Python program to move spaces to the front of a given string.
'''

# my solution
def move_Spaces_front(str1):
    space_li=[]
    chr_li=[]
    li=list(str1)
    for chr in li:
        if chr == ' ':
            space_li.append(chr)
        else:
            chr_li.append(chr)
    return "".join(space_li+chr_li)
print(move_Spaces_front("w3resource .  com  "))
print(move_Spaces_front("   w3resource.com  "))