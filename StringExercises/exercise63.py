'''
Write a Python program to remove leading zeros from an IP address.
output:
255.24.1.1
127.0.0.1
'''

# my solution
def remove_zeros_from_ip(str1):
    li = str1.split(".")
    ip_addr=""
    for elem in li:
        if len(elem) == 1: ip_addr+=elem+"."
        elif len(elem) >= 1 and not("0" in elem): ip_addr+=elem+"."
        else: ip_addr+=elem[1:]+"."
    return ip_addr[0:-1]
print(remove_zeros_from_ip("255.024.01.01"))
print(remove_zeros_from_ip("127.0.0.01 "))