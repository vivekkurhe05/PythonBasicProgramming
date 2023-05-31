'''
Write a Python program to read first n lines of a file.
'''

# my solution
def file_read_from_head(filename, num):
    try:
        file=open(filename,"rt")
        for i in range(0,num):
            print(file.readline())
        file.close()
    except:
        print("File does not exist")
file_read_from_head('text.txt',2)