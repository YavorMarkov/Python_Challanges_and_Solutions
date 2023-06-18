# Challenge_3 Easter vacation

# Read the destination, booked_dates, and num_nights from the input
destination = input()
booked_dates = input()
num_nights = int(input())

# Dictionary with destination and corresponding prices per night
prices = {
    "France": {"21-23": 30, "24-27": 35, "28-31": 40},
    "Italy": {"21-23": 28, "24-27": 32, "28-31": 39},
    "Germany": {"21-23": 32, "24-27": 37, "28-31": 43}
}

# Calculate the excursion cost by multiplying the number of nights with the price per night
excursion_cost = num_nights * prices[destination][booked_dates]

# Format the excursion cost to have two decimal places
excursion_cost_formatted = "{:.2f}".format(excursion_cost)

# Print the result with the destination and formatted excursion cost
print(f"Easter trip to {destination}: {excursion_cost_formatted} leva.")

# EXPLANATIONS:

# 1. The code reads the input for destination, booked_dates, and num_nights using the input() function.
# 2. The prices dictionary stores the prices per night for each destination and the corresponding dates.
# 3. The excursion cost is calculated by multiplying the number of nights (num_nights) with the price per night based on the destination (prices[destination][booked_dates]).
# 4. The excursion cost is formatted to have two decimal places using the "{:.2f}".format() function.

# 5. Finally, the result is printed on the console with the destination and the formatted excursion cost.