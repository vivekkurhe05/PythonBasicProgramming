# Replace string
# In JS, we use replaceAll() to replace all the same occurrences
data="hello this is testing world this"
print(data.replace('is','**'))
print(data.replace("world", "python"))
print(data.replace("l","L"))

print(len(data))
print(len(data.replace(" ", "")))

# Find data in a string
# In JS, we use indexOf()
# In python also, it returns -1 if string is not found, else it returns an index of the first match
print(data.find("this"))

# split string into a list of substrings
# In JS also, we use split()
result = data.split(" ")
print(result)

# convert string into list
data="1,2,3,4"
li=data.split(",")
print(li)

# convert string into tuple
# first convert string to list and then list to tuple
data="1,2,3,4"
li=data.split(',')
tu=tuple(li)
print(tu)