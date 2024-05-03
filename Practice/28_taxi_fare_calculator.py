# Create a program that calculates the total fare of a taxi ride based on distance and time.

distance = float(input("Enter distance (in kilometer) :"))
time = float(input("Enter time (in minutes) :"))

# Calculate fare based on distance and time
base_fare = 5.0
fare_per_km = 2.0
fare_per_min = 0.1

total_fare = base_fare + (distance * fare_per_km) + (time * fare_per_min)

print("Total fare: $", total_fare)
