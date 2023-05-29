'''
Write a Python program that capitalizes the first letter and lowercases the
remaining letters in a given string.
Sample Data:
("Red Green WHITE") -> "Red Green White"
("w3resource") -> "W3resource"
("dow jones industrial average") -> "Dow Jones Industrial Average"
'''

# my solution
def capitalize(str1):
    if not(str1 == str1.istitle()):
        str1=str1.title()
    return str1
print(capitalize("Red Green White"))
print(capitalize("W3resource"))
print(capitalize("Dow Jones Industrial Average"))