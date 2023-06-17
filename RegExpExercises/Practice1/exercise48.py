'''
Write a Python program to check a decimal with a precision of 2.
'''
# my solution
import re
def is_decimal(input):
    matchObj=re.search(r'^\d+(.\d{1,2})?$', input)
    return bool(matchObj)
print(is_decimal('123.11')) # True
print(is_decimal('123.1')) # True
print(is_decimal('123')) # True
print(is_decimal('0.21')) # True

print(is_decimal('123.1214')) # False
print(is_decimal('3.124587')) # False
print(is_decimal('e666.86')) # False