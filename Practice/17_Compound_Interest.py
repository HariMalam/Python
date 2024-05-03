# 17. Write a program that calculates the compound interest.

# Get principal amount, rate, and time from the user
principal = float(input("Enter the principal amount :"))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time period (years): "))

# Calculate compound interest using the formula
compound_interest = principal * (1 + rate / 100) ** time - principal

# Print the calculated compound interest
print("Compound Interest:", compound_interest)
