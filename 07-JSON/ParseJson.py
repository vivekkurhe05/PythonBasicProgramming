import json

# convert json string to python dictionary
json_string = '{"K1":"Val1","K2":"Val2"}'
json_to_dict = json.loads(json_string)
print(json_to_dict)
print(type(json_to_dict))

# In JS, we use JSON.parse()

# convert python dictionary to json string
di = {
    "K1":"Val1",
    "K2":"Val2"
}
json_string=json.dumps(di)
print(json_string)
print(type(json_string))