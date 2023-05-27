'''
Write a Python program to find the smallest and largest words in a given string.
'''

# my solution
def myFunc(e):
    return len(e)
def find_smallest_largest(str1):
    li = str1.split(" ")
    li.sort(key=myFunc)
    return li[0], li[-1]
print(find_smallest_largest("Write a Java program to sort an array of given integers using Quick sort Algorithm."))