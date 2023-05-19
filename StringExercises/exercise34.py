'''
Write a Python program to print the following integers with '*' to the right of the specified width.
'''

# may solution
def pad_end(n):
    n=str(n)
    num = len(n)*2
    while len(n) < num:
        n = n+"*"
    return n

print(pad_end(3))
print(pad_end(123))