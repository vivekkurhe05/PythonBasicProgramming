'''
Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
'''
import re

dt1 = "2026-01-02"
text=re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})',"\\3-\\2-\\1",dt1)
print(text)