# keyword arguments
def takeInput(a,b):
    c=a+b
    print("Value of a "+str(a))
    print("Value of b "+str(b))
    print("Sum is "+str(c))

takeInput(b=10,a=20)

# Default argument
def takeDefaultArgument(a,b=10):
    c=a+b
    print("Sum is "+str(c))

takeDefaultArgument(50)