'''
Write a Python program to extract and display the name from a given Email address.
Sample Data:
("john@example.com") -> ("john")
("john.smith@example.com") -> ("johnsmith")
("fully-qualified-domain@example.com") -> ("fullyqualifieddomain")
'''

# my solution
def display_name(str1):
    str2=str1[:str1.find("@")]
    name=""
    for chr in str2:
        if chr.isalpha():
            name+=chr
    return name

print(display_name("john@example.com"))
print(display_name("john.smith@example.com"))
print(display_name("fully-qualified-domain@example.com"))