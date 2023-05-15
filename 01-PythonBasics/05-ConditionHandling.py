# Take input from user - Number
# Check this number is even, Print this is even number
# Dont do anything if number is odd

num = input("Please enter a number: ")
num = int(num)
if num % 2 == 0:
    print("This is even number")
    print("This is my second line")
    print("End of Condition")

print("This is a print statement outside if condition")

# Take input from user - Number
# Check this number is even, Print this is even number
# Number is not Even, Print Odd Number

data = input("Please enter a number: ")
data = int(data)

if data % 2 == 0:
    print("This is even number")
else:
    print("This is Odd Number")


# Take input from user - Number
# Check Number is Negative - Print this is Negative Number
# Check Number is Zero - Print it is 0
# Check if it is Positive, only then check Even or Odd

data = input("Please enter a number: ")
data = int(data)

if data < 0:
    print("This is negative number")
elif data == 0:
    print("This is zero")
else:
    print("It is positive number")