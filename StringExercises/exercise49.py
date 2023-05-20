'''
Write a Python program to count and display vowels in text.
'''

# my solution
def count_and_display_vowels(str1):
    vowels='aeiouAEIOU'
    count=0
    li=[]
    for i in str1:
        if i in vowels:
            count+=1
            li.append(i)
    print(count)
    print(li)
count_and_display_vowels("welcome to w3resource.com")