import json

import jsonpath
import requests

# API URL
url = "https://reqres.in/api/users/2"

# Read input json file
file=open("CreateUser.json","r")
json_input=file.read()
request_body=json.loads(json_input)

# Make PUT request with Json input body
response=requests.put(url,request_body)

# Validating response code
# In case of PUT, response code is 200
assert response.status_code == 200

# Parse json string to dict
response_json=json.loads(response.text)
updated_li=jsonpath.jsonpath(response_json,"updatedAt")
print(updated_li[0])