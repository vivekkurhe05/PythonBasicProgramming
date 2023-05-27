'''
Write a Python program to capitalize the first and last letters of each word in a given string.
'''

# work on this
def capitalize_first_last_letters(str1):
    li=str1.split(" ")
    new_str=""
    for el in li:
        new_str+=el[0].upper()+el[1:-1]+el[-1].upper()+" "
    return new_str
print(capitalize_first_last_letters("python exercises practice solution"))
print(capitalize_first_last_letters("w3resource"))