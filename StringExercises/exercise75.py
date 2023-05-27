'''
Write a Python program to find the smallest window that contains all characters in a given string.
asdaewsqgtwwsa
'''

# jugadu solution
def find_sub_str(str1):
    counts={}
    li=[]
    for chr in str1:
        count = 1
        if chr in counts:
            count+=1
        counts[chr]=count
    for chr in counts:
        if counts[chr] == 1:
            li.append(chr)
    first_chr=li[0]
    last_chr=li[-1]

    return str1[str1.find(first_chr):str1.find(last_chr)+1]
print(find_sub_str("asdaewsqgtwwsa"))
print(find_sub_str("utewuectbgw"))

# uniq_chr=
# counts={u:2,t:2,e:2,w:2,c:1,b:1,g:1}
# expected-wuectbg