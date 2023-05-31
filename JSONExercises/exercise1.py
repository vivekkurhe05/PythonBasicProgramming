'''
Write a Python program to convert JSON data to Python object.
'''
# my solution
import json

json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
di=json.loads(json_obj)
print(di)
print(type(di))