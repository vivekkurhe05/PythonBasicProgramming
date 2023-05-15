# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

filename="abc.java"
extension=filename.split(("."))
ext=repr(extension[-1])
print(ext)
print(type(ext))