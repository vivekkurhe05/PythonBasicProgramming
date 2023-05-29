import json

import jsonpath
import requests

# API URL
url = "https://reqres.in/api/users"

# Read input json file
file=open("CreateUser.json","r")
json_input=file.read()
request_body=json.loads(json_input)

# Make POST request with Json input body

response=requests.post(url,request_body)

# Validating response code
assert response.status_code == 201

# Fetch headers from response
print(response.headers.get('Content-Length'))

# Parse json response
response_json=json.loads(response.text)
print(response_json)
print(type(response_json))

# Pick Id using jsonpath
id=jsonpath.jsonpath(response_json,"id")
print(id[0])

'''
Note
response.text is the content of the response in Unicode, 
and response.content is the content of the response in bytes.

response.text would be preferred for textual responses, such as an HTML or XML document
response.content would be preferred for "binary" filetypes, such as an image or PDF file.
'''