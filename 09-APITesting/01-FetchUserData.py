import jsonpath
import requests
import json

# API URL
url = "https://reqres.in/api/users?page=2"

# Send GET Request
response = requests.get(url)
print(response) # returns status code
print(response.content) # returns contents of the response
print(response.headers) # returns headers of the response
print(response.headers.get('Date')) # returns specific content from headers
print(response.headers.get('Server')) # returns specific content from headers

# validate status code
print(response.status_code)

# Fetch cookies
print(response.cookies)

# Fetch Encoding
print(response.encoding)

# Elapsed time - It is the time taken between request sent and response received
print(response.elapsed)

# Parse response to Json format
json_response = json.loads(response.content)
print(json_response)
print(json_response['data'][0]['email'])

# Fetch value using jsonpath
email = jsonpath.jsonpath(json_response,"data[0]['email']")
print(email[0])

for i in range(0,3):
    first_name = jsonpath.jsonpath(json_response,"data["+str(i)+"].first_name")
    print(first_name[0])

# this package by defaults comes with python
assert response.status_code == 200

assert email[0] == 'michael.lawson@reqres.in'