'''
Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module
'''
import calendar

year=int(input("Input the year: "))
month=int(input("Input the month: "))
print(calendar.month(year,month))