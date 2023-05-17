'''
Write a Python program to check whether a string starts with specified characters.
'''

# my solution
def startswith(string):
    return string.startswith("w3r")
print(startswith("w3resource"))

# or my solution

def startswith(string):
    return string.find("w3r") == 0
print(startswith("w3resource"))

# or my solution

def startswith(string):
    try:
        return string.index("w3r") == 0
    except:
        return "String does not start with a specified string"
print(startswith("w3resource"))