# Chalange 2. Shooting day


# We're importing the math module because we need to use the math.ceil() function later in the code.
import math

# This function calculates the preparation time based on the snapshot time.
# It's a simple multiplication: snapshot_time * 0.15.
# The snapshot_time parameter is given to the function when it's called.
def calculate_preparation_time(snapshot_time):
    return snapshot_time * 0.15

# This function calculates the total scene time based on the number of scenes and the duration of each scene.
# It's a simple multiplication: number_of_scenes * scene_duration.
# Both parameters are given to the function when it's called.
def calculate_total_scene_time(number_of_scenes, scene_duration):
    return number_of_scenes * scene_duration

# This function calculates the remaining time by subtracting the total time needed from the snapshot time.
# Both parameters are given to the function when it's called.
def calculate_remaining_time(snapshot_time, total_time_needed):
    return snapshot_time - total_time_needed

# This function prints the result based on the remaining time.
# If there's enough remaining time (remaining_time >= 0), it prints a success message.
# If there isn't enough remaining time (remaining_time < 0), it prints a failure message.
# The remaining_time parameter is given to the function when it's called.
def print_result(remaining_time):
    if remaining_time >= 0:
        print(f"You managed to finish the movie on time! You have {math.ceil(remaining_time)} minutes left!")
    else:
        print(f"Time is up! To complete the movie you need {math.ceil(abs(remaining_time))} minutes.")

# Input section of the code.
# We're reading the snapshot time, number of scenes, and scene duration from the console.
# The int() function is used to convert these inputs to integers since input() only reads strings.
snapshot_time = int(input())
number_of_scenes = int(input())
scene_duration = int(input())

# Calculation section of the code.
# We're calling our functions here with the appropriate arguments.
# The results of these function calls are stored in variables.
preparation_time = calculate_preparation_time(snapshot_time)
total_scene_time = calculate_total_scene_time(number_of_scenes, scene_duration)
total_time_needed = preparation_time + total_scene_time
remaining_time = calculate_remaining_time(snapshot_time, total_time_needed)

# Output section of the code.
# We're calling our print_result() function with the remaining_time variable.
print_result(remaining_time)
