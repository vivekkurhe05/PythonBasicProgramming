'''
Write a Python program to swap cases in a given string.
Sample Output:
pYTHON eXERCISES
jAVA
nUMpY
'''

# my solution
def swap_case(str1):
    return str1.swapcase()
print(swap_case("pYTHON eXERCISES"))
print(swap_case("jAVA"))
print(swap_case("nUMpY"))

# or my solution
def swap_case2(str1):
    new_str=""
    for chr in str1:
        if chr == chr.upper(): new_str+=chr.lower()
        else: new_str+=chr.upper()
    return new_str
print(swap_case2("pYTHON eXERCISES"))
print(swap_case2("jAVA"))
print(swap_case2("nUMpY"))