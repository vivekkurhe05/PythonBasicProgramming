'''
Write a Python function to convert a given string to all uppercase
if it contains at least 2 uppercase characters in the first 4 characters.
'''

# my solution
def to_uppercase(string):
    count=0
    for i in range(0,len(string[:4])):
        if("A"<=string[i] and string[i]<="Z"):
            count+=1
    if(count>=2): return string.upper()
    else: return string
print(to_uppercase('Python'))
print(to_uppercase('PyThon'))

# or w3resource solution

def to_uppercase2(string):
    count=0
    for i in range(0,len(string[:4])):
        if(string[i].upper() == string[i]):
            count+=1
    if(count>=2): return string.upper()
    else: return string
print(to_uppercase2('Java'))
print(to_uppercase2('JaVa'))