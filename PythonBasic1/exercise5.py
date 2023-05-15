# Write a Python program that accepts the user's first and
# last name and prints them in reverse order with a space between them.

name = "Vivek kurhe"
li = name.split(" ")
li.reverse()

reverse_str = ''
for elem in li:
    reverse_str+=" "+elem

print(reverse_str.lstrip())

print(type(li) == set)