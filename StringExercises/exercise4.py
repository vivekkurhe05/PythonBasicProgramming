'''
Write a Python program to get a string from a given string where all occurrences
of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''

# my solution
def changeAllOccurrencesOfFirstChar2(str):
    newStr=""
    for i in range(0,len(str)):
        if(str[i] == "r" and i == 0):
            newStr+=str[i]
        elif (str[i] == "r" and i != 0):
            newStr+="$"
        else:
            newStr+=str[i]
    return newStr

print(changeAllOccurrencesOfFirstChar2("restart"))