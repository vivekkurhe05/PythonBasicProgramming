'''
Write a Python program to count Uppercase, Lowercase, special characters and
numeric values in a given string.
'''

# my solution
def count(str1):
    upper_count, lower_count, numeric_count, special_count=0, 0, 0, 0
    for chr in str1:
        if chr >= 'A' and chr <= 'Z':
            upper_count+=1
        elif chr >= 'a' and chr <= 'z':
            lower_count+=1
        elif chr >= '0' and chr <= '9':
            numeric_count+=1
        else:
            special_count+=1
    return {
        'upperCase': upper_count,
        'lowerCase': lower_count,
        'numbers': numeric_count,
        'special': special_count
    }

print(count("@W3Resource.Com"))