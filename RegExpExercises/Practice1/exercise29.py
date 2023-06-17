'''
Write a Python program to separate and print the numbers and their position in a given string.
'''
# my solution
import re

text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
matches=re.finditer(r'\d+',text)
for match in matches:
    print(match.start())