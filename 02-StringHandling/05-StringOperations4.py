data='  hello this is testing world  '
print(len(data))

# trim space from start of the string
# In JS, we use trimStart()
print(len(data.lstrip()))

# trip space from end of the string
# In JS, we use trimEnd()
print(len(data.rstrip()))

# trim spaces from start and end of a string
# In JS, we use trim()
print(len(data.strip()))