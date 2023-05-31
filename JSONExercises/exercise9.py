'''
Write a Python program to access only unique key value of a Python object.
'''
# my solution
import json
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'

python_obj=json.loads(python_obj)
print(python_obj)