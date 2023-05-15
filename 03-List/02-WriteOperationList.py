# Write operation on list
# Update value from the list
programmingLanguage=[2021,'Java','C#','Python',True,False]
programmingLanguage[1]='JS'
print(programmingLanguage)

# Insert value to list
# In JS, we use splice(pos,elem_to_insert)
programmingLanguage.insert(2, "PHP Language")
print(programmingLanguage)

# Delete value from the list
# In JS, we use splice(pos,1)
programmingLanguage.remove("C#")
print(programmingLanguage)