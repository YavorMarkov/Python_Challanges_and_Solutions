# Function to calculate the count of eggs for each color
def count_eggs(egg_colors):
    """
    This function takes a list of egg colors and returns the count of eggs for each color.
    It uses the count() method of lists to count the occurrences of each color in the list.
    """
    return egg_colors.count("red"), egg_colors.count("orange"), egg_colors.count("blue"), egg_colors.count("green")

# Function to find the color with the maximum number of eggs
def find_max_color(egg_counts):
    """
    This function takes a tuple of egg counts for each color and returns the color with the maximum count.
    It finds the maximum count using the max() function and then uses a dictionary to map the count to the corresponding color.
    """
    max_count = max(egg_counts)
    max_color = {
        egg_counts[0]: "red",
        egg_counts[1]: "orange",
        egg_counts[2]: "blue",
        egg_counts[3]: "green"
    }[max_count]
    return max_count, max_color

# Read the total number of painted eggs
total_eggs = int(input())

# Read the color of each egg and create a list of colors
egg_colors = [input() for _ in range(total_eggs)]

# Count the number of eggs for each color using the count_eggs() function
red_count, orange_count, blue_count, green_count = count_eggs(egg_colors)

# Find the color with the maximum number of eggs using the find_max_color() function
max_count, max_color = find_max_color([red_count, orange_count, blue_count, green_count])

# Print the count of eggs for each color and the color with the most eggs
print(f"Red eggs: {red_count}")
print(f"Orange eggs: {orange_count}")
print(f"Blue eggs: {blue_count}")
print(f"Green eggs: {green_count}")
print(f"Max eggs: {max_count} -> {max_color}")


# Explanation for functions:

# The count_eggs() function takes a list of egg colors as input and returns a tuple containing the count of eggs for each color. It uses the count() method of lists to count the occurrences of each color in the list.
# The find_max_color() function takes a tuple of egg counts for each color as input and returns a tuple containing the maximum count and the color with the maximum count. It finds the maximum count using the max() function and then uses a dictionary to map the count to the corresponding color.
# Explanation for main code:

# The total number of painted eggs is read from the input and stored in the variable total_eggs.
# The color of each egg is read from the input using a list comprehension, and a list of egg colors is created and stored in the variable egg_colors.
# The count_eggs() function is called with egg_colors as the argument, and the returned counts for each color are assigned to the variables red_count, orange_count, blue_count, and green_count.
# The find_max_color() function is called with a list containing the counts of each color as the argument, and the returned maximum count and color are assigned to the variables max_count and max_color.
# The count of eggs for each color and the color with the most eggs are printed using formatted strings.