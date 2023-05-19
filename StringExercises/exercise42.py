'''
Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
'''

# my solution
def count_repeated_chars(input):
    di = {}
    for i in range(0,len(input)):
        count = 0
        index=input.find(input[i])
        while not(index==-1):
            count+=1
            index=input.find(input[i],index+1)
            if count > 1:
                di[input[i]]=count
    for key in di:
        print(key+" "+str(di[key]))

count_repeated_chars("thequickbrownfoxjumpsoverthelazydog")