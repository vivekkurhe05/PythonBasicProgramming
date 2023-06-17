'''
Write a Python program to remove leading zeros from an IP address.
'''
# my solution
import re
ip = "216.08.094.196"
matchObj=re.search(r'0(?=\d)',ip)
print(ip.replace(matchObj.group(),""))

# or my solution

mObj=re.sub(r'0(?=\d)',"",ip)
print(mObj)