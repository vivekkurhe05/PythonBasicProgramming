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

# Pick Id using jsonpath
id=jsonpath.jsonpath(response_json,"id")
print(id[0])