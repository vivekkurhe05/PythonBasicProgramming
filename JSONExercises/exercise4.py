'''
Write a Python program to convert Python dictionary object (sort by key) to JSON data.
Print the object members with indent level 4
'''
# my solution
import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
res_json=json.dumps(j_str, indent=4, sort_keys=True)
print(res_json)