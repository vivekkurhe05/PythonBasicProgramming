'''
Write a Python program to find the minimum window in a given string that will contain
all the characters of another given string.
Example 1
Input : str1 = " PRWSOERIUSFK "
str2 = " OSU "
Output: Minimum window is "OERIUS
'''

# my solution
def minimum_window(str1,str2):
    char=str2[0]
    li=[]
    index1=str1.find(char)
    str3=str1[index1:]
    for chr in str2:
        index=str3.find(chr)
        li.append(index)
    li.sort()
    last_index=li[2]
    return str3[:last_index+1]
print(minimum_window("PRWSOERIUSFK","OSU"))