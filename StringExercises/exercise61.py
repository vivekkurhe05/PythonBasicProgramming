'''
Write a Python program to remove duplicate characters from a given string.
python exrcisalu
w3resouc
'''

# my solution
def remove_duplicate(str1):
    unique_str=""
    for chr in str1:
        if not (chr in unique_str):
            unique_str+=chr
    return unique_str
print(remove_duplicate("python exercises practice solution"))
print(remove_duplicate("w3resource"))