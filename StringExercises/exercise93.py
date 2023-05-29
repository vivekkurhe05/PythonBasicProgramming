'''
Write a Python program to extract numbers from a given string.
Sample Output:
Original string: red 12 black 45 green
Extract numbers from the said string: [12, 45]
'''

# my solution
def extract_numbers(str1):
    li=str1.split(" ")
    li2=[]
    for elem in li:
        if elem.isdigit():
            li2.append(int(elem))
        else:
            continue
    return li2
print(extract_numbers("red 12 black 45 green"))