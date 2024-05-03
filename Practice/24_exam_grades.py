# Create a program that categorizes a given exam score into grades (A, B, C, etc.).

marks = float(input("Enter you marks :"))

if marks > 90:
    grade = "A"
elif marks > 80:
    grade = "B"
elif marks > 70:
    grade = "C"
elif marks > 60:
    grade = "D"
elif marks > 50:
    grade = "E"
else:
    grade = "F"

print("The grade is", grade)
