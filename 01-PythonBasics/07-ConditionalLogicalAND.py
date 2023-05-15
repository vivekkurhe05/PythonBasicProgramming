# Take 1 number from user
# Check if number is +ve and multiple of 2, then print even number
# Check if number is +ve and not multiple of 2, then print odd number

num = input("Please enter a number: ")
num = int(num)

if num >=0 and num % 2 == 0:
    print("This is positive Even Number")
elif num>=0 and num % 2 == 1:
    print("This is positive Odd Number")