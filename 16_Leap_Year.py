# 16. Create a program that determines whether a given year is a leap year or not.

year = int(input("Enter a Year :"))

# Check for leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
