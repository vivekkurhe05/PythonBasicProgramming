'''
Write a Python program to convert Python object to JSON data.
'''
# my solution
import json

python_obj = {
  "name": "David",
  "class":"I",
  "age": 6
}

json_response=json.dumps(python_obj, indent=4)
print(json_response)
print(type(json_response))