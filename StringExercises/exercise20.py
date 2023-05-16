'''
Write a Python function to reverse a string if its length is a multiple of 4.
'''

# my solution
# still need to work on it
def reverse_string(string):
    if(len(string)%4==0):
        li=list(string)
        li.reverse()
        return "".join(li)
    return string
print(reverse_string('abcd'))
print(reverse_string('python'))