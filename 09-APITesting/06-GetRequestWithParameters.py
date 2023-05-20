import requests

# Create dictionary of parameters
# Send parameters with request
param={'name':'Vivek','email':'vivek.kurhe@gmail.com','number':'8909878899'}
response=requests.get("https://httpbin.org/get",params=param)
print(response.text)