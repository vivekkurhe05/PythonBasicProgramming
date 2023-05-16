# Created with __init__, first argument is always self
# Automatically called when object is created
# Can take arguments
# Constructor never returns any value
# Constructors are used for initialization

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("My name is "+self.name)
        print("I am "+str(self.age)+" years old")

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
p1.info()