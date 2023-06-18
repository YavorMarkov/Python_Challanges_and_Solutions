# Challenge1. Oscar ceremony 

# The United States Film Academy since 1929. annually hands out Academy Awards in a spectacular ceremony. The organizers want to know how much it costs to organize such a ceremony. Write a program that calculates what costs the academy will have to organize the event, knowing how much the rent is for the hall where it will be held.

# • Statuettes – their price is 30% less than the hall rent

# • Catering - its price is 15% less than that of the statuettes

# • Sound - its price is 1 / 2 of the price for catering

# INPUT

# 1 line is read from the console:

# · Rent for the hall - an integer in the interal [0 … 999]

# OUTPUT
# To print on the console what the costs of organizing the ceremony will be. Amount to be formatted to the second decimal place.


# We start by defining a function. A function is a reusable piece of code that performs a specific task.
# Our function is named 'calculate_costs' and it takes one parameter: 'rent'.
def calculate_costs(rent):
    # Inside the function, we first calculate the cost of the statuettes.
    # According to the problem, the statuettes cost 30% less than the rent. 
    # So, we take 70% (100% - 30%) of the rent to get the cost of the statuettes.
    statuettes = rent * 0.7

    # Next, we calculate the cost of the catering.
    # The problem states that the catering costs 15% less than the statuettes.
    # So, we take 85% (100% - 15%) of the cost of the statuettes to get the cost of the catering.
    catering = statuettes * 0.85

    # Then, we calculate the cost of the sound.
    # The problem says that the sound costs half as much as the catering.
    # So, we divide the cost of the catering by 2 to get the cost of the sound.
    sound = catering / 2

    # Now, we need to calculate the total cost of the ceremony.
    # This is the sum of the rent, the cost of the statuettes, the cost of the catering, and the cost of the sound.
    total_cost = rent + statuettes + catering + sound

    # We want to return the total cost as a string, formatted to the second decimal place.
    # The '{:.2f}'.format(total_cost) part of the code does this formatting for us.
    return "{:.2f}".format(total_cost)

# Outside the function, we ask the user to enter the rent for the hall.
# We use the 'input' function to get the user's input, and 'int' to convert that input into an integer.
rent = int(input("Enter the rent for the hall: "))

# Finally, we call our function with the rent value that the user entered.
# We print out the result, which is the total cost of organizing the ceremony.
print("The total cost of organizing the ceremony will be: $", calculate_costs(rent))


# This code is a complete program that reads the rent from the user, calculates the total cost of the ceremony, and prints out the result. The calculations are done inside the calculate_costs function, which can be reused in other parts of the program if needed