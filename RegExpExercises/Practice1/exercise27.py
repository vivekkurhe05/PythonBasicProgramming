'''
Write a Python program to separate and print the numbers in a given string.
'''
# my solution
import re

text = "Ten 10, Twenty 20, Thirty 30"
li=re.findall(r'\d+', text)
print(li)