'''
Write a Python program to count the occurrences of each word in a given sentence.
Sample String : "the quick brown fox jumps over the lazy dog"
'''

# my solution
def word_count(string):
    di={}
    li = string.split(" ")
    for word in li:
        count=0
        index=string.find(word,0)
        while(not(index == -1)):
            count+=1
            index=string.find(word,index+1)
            di[word] = count
    return di
print(word_count("the quick brown fox jumps over the lazy dog"))