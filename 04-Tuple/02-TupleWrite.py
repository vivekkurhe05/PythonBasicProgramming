# define a tuple
programmingLanguage=(2021,"C#","Java","Python",True,False)
new_programming=("PHP","Groovy")

final_tuple=programmingLanguage+new_programming
print(final_tuple)

# tuple does not support update operation
# programmingLanguage[2]="JS"
# print(programmingLanguage)

# tuple does not support remove operation
# Only this way you can delete value from tuple, it's a new tuple not the existing one
print(programmingLanguage[:1]+programmingLanguage[2:])