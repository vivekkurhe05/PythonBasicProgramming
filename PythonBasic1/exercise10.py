'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''

n = int(input("Please enter a number: "))
n1 = int('%s'%n)
n2 = int("%s%s"%(n,n))
n3 = int("%s%s%s"%(n,n,n))
sum = n1+n2+n3
print(sum)