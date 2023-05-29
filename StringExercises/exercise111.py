'''
Write a Python program that takes a string and replaces all the characters with their respective numbers.
Sample Data:
("Python") -> "16 25 20 8 15 14"
("Java") -> "10 1 22 1"
("Python Tutorial") -> "16 25 20 8 15 14 20 21 20 15 18 9 1 12"
'''

# my solution
def replace_by_num(str1):
    alpha="abcdefghijklmnopqrstuvwxyz"
    str1=str1.lower()
    result=""
    for chr in str1:
        if chr in alpha:
            result+=" "+str(alpha.find(chr)+1)
    return result
print(replace_by_num("Python"))
print(replace_by_num("Java"))
print(replace_by_num("Python Tutorial"))