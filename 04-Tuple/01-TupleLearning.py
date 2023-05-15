# define a tuple
programmingLanguage=(2021,"C#","Java","Python",True,False)

# Display all values of Tuple
print(programmingLanguage)

# Fetch any specific value from tuple by giving index
print(programmingLanguage[3])
print((programmingLanguage[3:6]))
print(programmingLanguage[2:])
print(programmingLanguage[:3])

# Find length of the tuple
print(len(programmingLanguage))

# tuple using for loop - approach 1
for i in range(0, len(programmingLanguage)):
    print(programmingLanguage[i])

print("=======================================")

# tuple using for loop - approach 2
for elem in programmingLanguage:
    print(elem)