# Take marks from user and check, if it is > 100 or < 0, this is invalid marks
# If number is between 0-100, display valid marks

# Conditional OR

marks = input("Please enter your subject marks: ")
marks = float(marks)

if marks > 100 or marks < 0:
    print("This is invalid marks")
else:
    print("Marks are "+str(marks))