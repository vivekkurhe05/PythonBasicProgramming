# Printing data multiple times
# in JS we use, repeat()
a="hello"
print(a*3)

# Fetch substring by giving start and end index
# In JS, we use substring(startIndex, endIndex), substr(startIndex, length), slice(startIndex, endIndex)
data="this is testing world"
print(data[2:9])

# Casing of string and length of string
# In JS, we use length property
data='this is start of my learning'
print(len(data))

# Take my string to upper case
# In JS, we use toUpperCase(), toLocaleUpperCase()
print(data.upper())

# Take my string to lower case
# In JS, we use toLowerCase(), toLocaleLowerCase()
print(data.lower())

# Initialize character in upper case
# In JS, we use data.slice(0)
print(data.capitalize())

# trim space from start of the string
# In JS, we use trimStart()
print(len(data.lstrip()))

# trip space from end of the string
# In JS, we use trimEnd()
print(len(data.rstrip()))

# trim spaces from start and end of a string
# In JS, we use trim()
print(len(data.strip()))

# Replace string
# In JS, we use replaceAll() to replace all the same occurrences
print(data.replace('is','**'))
print(data.replace("world", "python"))
print(data.replace("l","L"))

print(len(data))
print(len(data.replace(" ", "")))

# Find data in a string
# In JS, we use indexOf()
# it returns -1 if string is not found, else it returns an index of the first match
print(data.find("this"))

# split string into a list of substrings
# In JS also, we use split()
result = data.split(" ")
print(result)