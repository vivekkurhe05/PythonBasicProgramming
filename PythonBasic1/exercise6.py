'''
Write a Python program that accepts a sequence of comma-separated numbers
from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''

data="1,2,3,4"
li=data.split(",")
print(li)
print(type(li))

tu2=tuple(li)
print(tu2)
print(type(tu2))

