# Chalange 2. Shooting day

# You are the director of the movie "Programming is Fun" with a fixed time for shooting. You are asked to write a program that will tell you if you will have time to shoot the film on the day of shooting. The shooting day begins with field preparation, which is 15 percent of shooting time! A film has a certain number of scenes that are shot in a certain amount of time.

# INPUT

# 3 lines are read from the console:

# 1. Snapshot time - an integer in the range [0… 1440]

# 2. Number of scenes - an integer in the range [5… 25]

# 3. Scene duration - an integer in the range [20… 90]

# OUTPUT

# To print one line to the console:

# · If you run out of film time:

# "You managed to finish the movie on time! You have {remaining time} minutes left!"

# · If the time is NOT enough for YOU:

# "Time is up! To complete the movie you need minutes."

# Round the remaining time to the nearest whole number.





import math

# Input
snapshot_time = int(input())  # Read the snapshot time from the console and convert it to an integer
number_of_scenes = int(input())  # Read the number of scenes from the console and convert it to an integer
scene_duration = int(input())  # Read the scene duration from the console and convert it to an integer

# Calculation
preparation_time = snapshot_time * 0.15  # Calculate the preparation time, which is 15% of the snapshot time
total_scene_time = number_of_scenes * scene_duration  # Calculate the total time required for all the scenes

total_time_needed = preparation_time + total_scene_time  # Calculate the total time needed to finish shooting the movie
remaining_time = snapshot_time - total_time_needed  # Calculate the remaining time after subtracting the total time needed

# Output
if remaining_time >= 0:
    # If the remaining time is non-negative, it means there is enough time to finish the movie
    # Use math.ceil to round up the remaining time to the nearest whole number
    print(f"You managed to finish the movie on time! You have {math.ceil(remaining_time)} minutes left!")
else:
    # If the remaining time is negative, it means there isn't enough time to finish the movie
    # Use math.ceil and abs to round up the absolute value of the remaining time to the nearest whole number
    print(f"Time is up! To complete the movie you need {math.ceil(abs(remaining_time))} minutes.")
