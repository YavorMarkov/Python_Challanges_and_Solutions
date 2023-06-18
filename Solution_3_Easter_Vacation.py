# Challenge_3 Easter vacation

# Define a function to read user inputs
def get_user_input():
    # Use Python's built-in function 'input' to get user inputs.
    # These inputs are the destination, booked_dates, and num_nights.
    destination = input()
    booked_dates = input()
    num_nights = int(input())  # Convert the input to an integer since it's a numerical value
    return destination, booked_dates, num_nights  # Return these inputs for later use

# Define a function to calculate the excursion cost
def calculate_excursion_cost(destination, booked_dates, num_nights, prices):
    # Calculate the excursion cost by multiplying the number of nights by the price per night
    # The price per night is retrieved from the 'prices' dictionary using 'destination' and 'booked_dates' as keys
    return num_nights * prices[destination][booked_dates]

# Define a function to format the excursion cost
def format_excursion_cost(excursion_cost):
    # Format the calculated excursion cost to two decimal places using the "{:.2f}".format() function
    return "{:.2f}".format(excursion_cost)

# Define a function to print the result
def print_result(destination, excursion_cost_formatted):
    # Print the result in the specified format using an f-string for better readability
    print(f"Easter trip to {destination}: {excursion_cost_formatted} leva.")

# The main program
def main():
    # Define a dictionary that contains the prices per night for each destination and date
    prices = {
        "France": {"21-23": 30, "24-27": 35, "28-31": 40},
        "Italy": {"21-23": 28, "24-27": 32, "28-31": 39},
        "Germany": {"21-23": 32, "24-27": 37, "28-31": 43}
    }

    # Get user inputs by calling the 'get_user_input' function
    destination, booked_dates, num_nights = get_user_input()

    # Calculate the excursion cost by calling the 'calculate_excursion_cost' function
    excursion_cost = calculate_excursion_cost(destination, booked_dates, num_nights, prices)

    # Format the excursion cost by calling the 'format_excursion_cost' function
    excursion_cost_formatted = format_excursion_cost(excursion_cost)

    # Print the result by calling the 'print_result' function
    print_result(destination, excursion_cost_formatted)

# Execute the main program
if __name__ == "__main__":
    main()  # Call the 'main' function if this Python file is the main module

# This code is organized into several functions. By breaking the problem down into smaller parts (functions), it becomes easier to understand, debug, and maintain. Each function is responsible for a specific task and can be tested individually. The main function coordinates the overall program flow. Finally, the script checks if it is being run as a standalone program (not being imported as a module) before calling main.