'''
Write a Python function to get a string made of 4 copies of the last two characters
of a specified string (length must be at least 2).
Sample function and result :
insert_end('Python') -> onononon
insert_end('Exercises') -> eseseses
'''

# my solution
def insert_end(string,n):
    return string[len(string)-2:]*n
print(insert_end("Python",4))
print(insert_end("Exercises",4))