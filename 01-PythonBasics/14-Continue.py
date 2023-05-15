# continue statement

num=input("Please enter a number")
for i in range(1, 11):
    if(int(num)*i==60):
        continue
    print(int(num)*i)