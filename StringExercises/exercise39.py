'''
Write a Python program to reverse a string.
'''

# my solution
def reverse_string(input):
    li = list(input)
    li.reverse()
    return "".join(li)
print(reverse_string("w3resource"))
