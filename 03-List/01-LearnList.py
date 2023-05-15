# define a new list
programmingLanguage=[2021,'Java','C#','Python',True,False]

# Display complete data of the list
print(programmingLanguage)

# display length of the list
print(len(programmingLanguage))

for elem in programmingLanguage:
    if(type(elem) == str):
        print(elem)

# or

for i in range(0, len(programmingLanguage)):
    if(type(programmingLanguage[i]) == bool):
        print(programmingLanguage[i])



# Fetch data from list : index
print(programmingLanguage[3])
print(programmingLanguage[2:5])
print(programmingLanguage[2:])
print(programmingLanguage[:3])