'''
Write a Python program to print the following integers with zeros
to the left of the specified width.
'''

# my solution
def pad_start(n):
    n=str(n)
    num = len(n)*2
    while len(n) < num:
        n = "0"+n
    return n

print(pad_start(3))
print(pad_start(123))