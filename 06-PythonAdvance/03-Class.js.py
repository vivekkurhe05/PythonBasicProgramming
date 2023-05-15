# Python is an object oriented scripting language
# We can write our code in class
# Class can have variables, constants, functions, and constructors
# We can access class members by creating an object of a class

class A:
    def welcome(self):
        print("This is class function")

    def sum(self,a,b):
        c=a+b
        print("Sum is "+str(c))

    def mul(self,a,b):
        c=a*b
        return str(c)

obj = A()
obj.welcome()
obj.sum(2,3)
z=obj.mul(2,3)
print("Multiplication is "+z)