'''
Write a Python program to remove unwanted characters from a given string.
Sample Output:
Original String : Pyth*^on Exercis^es
After removing unwanted characters:
Python Exercises
Original String : A%^!B#*CD
After removing unwanted characters:
ABCD
'''

# my solution
def remove_unwanted_chars(str1):
    result=""
    for chr in str1:
        if chr.isalpha() or chr == " ":
            result+=chr
    return result

print(remove_unwanted_chars("Pyth*^on Exercis^es"))
print(remove_unwanted_chars("A%^!B#*CD"))