"""
Write a program that works out whether if a given year is a leap year.
A normal year has 365 days, leap years have 366, with an extra day in
February.

This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 **except** every year that
 is evenly divisible by 100 **unless** the year is also evenly divisible by 400
 
"""



year = int(input("Which year do you want to check?\n"))
division_by4 = year/4
division_by100 = year/100
division_by400 = year/400
if year%4 == 0 and year%100 ==0 and year%400==0:
    print (f"{year} is a leap year")
elif year%4 == 0 and year%100 ==0 and year%400!=0:
    print (f"{year} is not a leap year")
elif year%4 != 0:
    print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")


print(f"Divison by 4 is {division_by4}, division by 100 is {division_by100}, division by 400 is {division_by400}")