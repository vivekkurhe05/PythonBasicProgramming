# How to create function
# Rules to create a function
# def keyword is used to create a function
# First line of function is optional, can be used for commenting
# return keyword shows end of function

def testing():
    "This is first line and it is used for commenting"
    print("This is testing world")
    return

testing()

# Function with arguments
def sum(a,b):
    c=a+b
    return str(c)

print("Sum is "+sum(1,2))