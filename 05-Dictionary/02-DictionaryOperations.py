# Define dictionary
myDict = {"a":100,"b":200,"c":"HelloWorld"}

# Add value to dictionary
myDict["email"]="test@gmail.com"

# Update value in the dictionary
myDict["b"]="hi"

print(myDict)

# Delete value from dictionary
# In JS, we use delete objectname.propertyname
myDict.pop("b")
print((myDict))


# Fetch only keys from dictionary
# In JS, we use Object.keys(objectname)
print(myDict.keys())

# Fetch only values from dictionary
# In JS, we use Object.values(objectname)
print(myDict.values())