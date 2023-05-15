a="  Hello"
b="hello  "

if(a.strip() == b.strip()):
    print("Strings are same")
else:
    print("Strings are not same")


# Case insensitive comparison
if(a.strip().upper() == a.strip().upper()):
    print("Strings are same with case insensitive")
else:
    print("Strings are not same with case insensitive")