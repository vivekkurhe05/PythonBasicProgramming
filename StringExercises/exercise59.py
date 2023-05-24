'''
Write a Python program to find the first maximum number of characters in a given string.
'''
# noted
# my solution
def get_max_occuring_char(str1):

    di = {}
    for chr in str1:
        count = 1
        if chr in di:
            count=di[chr]+1
            di[chr]=count
        else:
            di[chr]=count
    li=[]
    max_num = 1
    for chr in di:
        if di[chr] <= max_num:
            pass
        else:
            li.append(chr)
            max_num=di[chr]
    return li
print(get_max_occuring_char("Python: Get file creation and modification date/times"))
print(get_max_occuring_char("abcdefghijkb"))

'''
P=1,y=1,t=6,h=1,o=4,n=4,:=1,' '=6,G=1,e=5,f=2,i=6,l=1,c=2,r=1,a=4,d=3,m=2,/=1,s=1
'''