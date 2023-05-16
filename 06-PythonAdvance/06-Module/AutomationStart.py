# Whenever we are importing any module, that module executable code will run
import PyModule

PyModule.hello()

# We need to create object of the class written in any module
obj=PyModule.A()
obj.hi()