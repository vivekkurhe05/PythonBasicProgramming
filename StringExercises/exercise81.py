'''
Write a Python program to determine the index of a given string at which a certain substring starts.
If the substring is not found in the given string return 'Not found'.
'''

# my solution
def find_Index(str1, substr):
    index=str1.find(substr)
    if(not(index==-1)):
        return index
    return "Not found"
print(find_Index("Python Exercises", "Ex"))
print(find_Index("Python Exercises", "yt"))
print(find_Index("Python Exercises", "PY"))