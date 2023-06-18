# Solutons_5 Darts


# Function to start the game
def play_darts():
    # Input for the player's name
    player_name = input().strip()

    # Initialize the total points and the counts for successful and unsuccessful throws
    total_points = 301
    successful_throws = 0
    unsuccessful_throws = 0

    # Start a loop that continues as long as total_points is more than 0
    while total_points > 0:
        # Input for the type of field hit
        field = input().strip()

        # If the field input is 'Retire', the player has decided to stop playing
        if field == 'Retire':
            # Print a message showing how many unsuccessful shots the player made before retiring
            print(f'{player_name} retired after {unsuccessful_throws} unsuccessful shots.')
            # Stop the function
            return

        # Input for the points scored in this shot
        points = int(input().strip())
        # If the field was 'Double', double the points
        if field == 'Double':
            points *= 2
        # If the field was 'Triple', triple the points
        elif field == 'Triple':
            points *= 3

        # If the points scored are less than or equal to the remaining points, 
        # subtract them from total_points and increment successful_throws
        if points <= total_points:
            total_points -= points
            successful_throws += 1
        # If the points scored are greater than the remaining points,
        # the throw is unsuccessful and increment unsuccessful_throws
        else:
            unsuccessful_throws += 1

    # If total_points is 0, the player has won
    # Print a message showing how many successful shots it took for the player to win
    print(f'{player_name} won the leg with {successful_throws} shots.')

# Call the function to start the game
play_darts()



# This program begins by receiving the player's name and setting up the initial conditions of the game: the starting points (301) and the number of successful and unsuccessful throws (both initially 0).

# Then it enters a loop where it continually accepts inputs of the field and points. If the field input is "Retire", the player is assumed to have retired from the game, and a retirement message is printed.

# Otherwise, the point value is calculated according to the field type ("Double" or "Triple"). If the points scored are less than or equal to the remaining points, they are subtracted from the total and the number of successful throws is incremented. If the points scored are greater than the remaining points, the throw is considered unsuccessful and the number of unsuccessful throws is incremented.

# The game ends when the total points reach 0, at which point a victory message is printed.