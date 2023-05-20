import requests

# Create Dictionary of Request headers
# Send customized headers with request
headerdata={'T1':'First_Header','T2':'Second_Header'}
response=requests.get("https://httpbin.org/get",headers=headerdata)
print(response.text)