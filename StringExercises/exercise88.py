'''
Write a Python program to check whether a given string contains a capital letter,
a lower case letter, a number and a minimum length.
Sample Output:
Input the string: W3resource
['Valid string.']
'''

# work on this
# w3resource solution
def is_criteria_matched(str1):
    messg = []
    if not any(x.isupper() for x in str1):
        messg.append('String must have at least 1 uppercase letter')
    elif not any(x.islower() for x in str1):
        messg.append('String must have at least 1 lowercase letter')
    elif not any(x.isdigit() for x in str1):
        messg.append('String must have at least 1 digit')
    elif len(str1) < 8:
        messg.append("String length should be at least 8")
    else:
         messg.append('Valid string.')
    return messg

print(is_criteria_matched("W3resource"))
print(is_criteria_matched("w3resource"))
print(is_criteria_matched("W3RESOURCE"))
print(is_criteria_matched("Wresource"))
print(is_criteria_matched("W3resou"))