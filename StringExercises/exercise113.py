'''
Write a Python program that returns a string sorted alphabetically by the first
character of a given string of words.
Sample Data:
("Red Green Black White Pink") -> "Black Green Pink Red White"
("Calculate the sum of two said numbers given as strings.") -> ("Calculate as given numbers of sum said strings. the two")
("The quick brown fox jumps over the lazy dog.") -> ("The brown dog. fox jumps lazy over quick the")
'''

# my solution
def myFunc(e):
    return e[0]
def sort_alphabetically(str1):
    li=str1.split(" ")
    li.sort(key=myFunc)
    return " ".join(li)
print(sort_alphabetically("Red Green Black White Pink"))
print(sort_alphabetically("Calculate the sum of two said numbers given as strings."))
print(sort_alphabetically("The quick brown fox jumps over the lazy dog."))