'''
Write a Python program to print the following numbers up to 2 decimal places.
'''


def upto_2_decimal_places(num):
    return "Formatted number: {:.2f}".format(num)
print(upto_2_decimal_places(3.1415926))
print(upto_2_decimal_places(12.9999))