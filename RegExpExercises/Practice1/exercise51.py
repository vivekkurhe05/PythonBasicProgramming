'''
Write a Python program to insert spaces between words starting with capital letters.
'''
# my solution
import re
def capital_words_spaces(text):
    return re.sub(r'(?=[A-Z])\B'," ",text)
print(capital_words_spaces("Python"))
print(capital_words_spaces("PythonExercises"))
print(capital_words_spaces("PythonExercisesPracticeSolution"))