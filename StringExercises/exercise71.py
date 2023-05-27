'''
Write a Python program to move all spaces to the front of a given string in a single traversal.
'''

# my solution
def move_spaces(str1):
    li=list(str1)
    for i in range(0,len(li)):
        if li[i] == " ":
            popped = li.pop(i)
            li.insert(0,popped)
    return "".join(li)

print(move_spaces("Python Exercises"))