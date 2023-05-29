import json

json_string = '{"K1":"Val1","K2":"Val2"}'
json_to_dict = json.loads(json_string) # converts json string into python dictionary
print(json_to_dict)
print(type(json_to_dict))

# In JS, we use JSON.parse()

di = {
    "K1":"Val1",
    "K2":"Val2",
    "C1":"Val4",
    "A1":"Val3"
}
json_string=json.dumps(di, indent=4, sort_keys=True) # converts python dictionary into json string
print(json_string)
print(type(json_string))