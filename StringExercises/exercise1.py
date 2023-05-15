# Write a Python program to calculate the length of a string.

# my solution
def calculate_string_length(str):
    return len(str)

print(calculate_string_length("w3resource.com"))

# or my solution

count=0
str='w3resource.com'
for i in str:
    count+=1

print(count)

# or my solution

def length(sample):
    try:
        length=0
        while(sample[length]):
            length+=1
    except:
        return length

print(length("w3resource.com"))