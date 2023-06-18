# Solutions 6 Easter Decorations
# Function to calculate the total bill for a customer's purchases
def calculate_bill(purchases):
    total_bill = 0
    
    # Loop over each item in the purchases list
    for purchase in purchases:
        # Check the type of each purchase and add the corresponding price to the total bill
        if purchase == "basket":
            total_bill += 1.50
        elif purchase == "wreath":
            total_bill += 3.80
        elif purchase == "chocolate bunny":
            total_bill += 7.00

    # If the total number of items purchased is an even number, apply a 20% discount on the total bill
    if len(purchases) % 2 == 0:
        total_bill *= 0.80
        
    return total_bill

# Function to handle each customer
def handle_client():
    purchases = []  # Initialize an empty list to store the purchases for each customer
    
    # Take user input for each purchase. Continue to take input until "Finish" command is given
    command = input()
    while command != "Finish":
        purchases.append(command)  # Add each purchase to the purchases list
        command = input()
        
    # Call calculate_bill function to calculate the total bill for the current customer
    total_bill = calculate_bill(purchases)
    
    # Print out the total number of items purchased and the total price, formatted to two decimal places
    print(f"You purchased {len(purchases)} items for {total_bill:.2f} leva.")
    return total_bill

# Main function to run the program
def main():
    total_money = 0  # Initialize a variable to store the total money spent by all customers
    total_clients = int(input())  # Take user input for the total number of customers

    # Loop over each customer and handle their purchases
    for _ in range(total_clients):
        total_money += handle_client()  # Add the total bill of each customer to the total money

    # Calculate the average bill per client by dividing the total money by the total number of clients
    average_bill = total_money / total_clients
    
    # Print out the average bill per client, formatted to two decimal places
    print(f"Average bill per client is: {average_bill:.2f} leva.")

# Call the main function to start the program
main()


#  the main() function initializes the total money and reads the total number of clients. It then goes into a loop to handle each client, adding the result to the total money.

# The handle_client() function reads each purchase until the "Finish" command is given, stores them in a list, calculates the bill, and returns it.

# The calculate_bill() function takes a list of purchases as an argument, calculates the bill, and returns it. If the total purchases are even, it applies a 20% discount to the bill.