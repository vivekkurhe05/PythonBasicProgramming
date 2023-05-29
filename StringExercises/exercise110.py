'''
Write a Python program to insert space before every capital letter appears in a given word.
Sample Data:
("PythonExercises") -> "Python Exercises"
("Python") -> "Python"
("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"
'''

# my solution
def insert_space(str1):
    str2=""
    for chr in str1:
        if chr==chr.upper():
            str2+=" "+chr
        else:
            str2+=chr
    return str2
print(insert_space("PythonExercises"))
print(insert_space("Python"))
print(insert_space("PythonExercisesPracticeSolution"))