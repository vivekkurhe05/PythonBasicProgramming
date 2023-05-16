'''
Write a Python program to sort a string lexicographically.
'''

# my solution
def lexicographi_sort(string):
    li=list(string)
    li.sort()
    return "".join(li)

print(lexicographi_sort("w3resource"))