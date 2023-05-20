'''
Write a Python program to find the first non-repeating character in a given string.
'''

# my solution
def first_non_repeating_character(str1):
    di={}
    li=[]
    for chr in str1:
        count=0
        index=str1.find(chr)
        while(not(index==-1)):
            count += 1
            index = str1.find(chr, index + 1)
            di[chr]=count
    for key in di:
        if di[key] >= 2:
            pass
        else:
            li.append(key)
    try:
        return li[0]
    except:
        return None

print(first_non_repeating_character('abcdef'))
print(first_non_repeating_character('abcabcdef'))
print(first_non_repeating_character('aabbcc'))