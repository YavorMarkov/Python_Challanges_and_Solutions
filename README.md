**Challenge 1: Oscar Ceremony**

The United States Film Academy has been annually organizing the prestigious Academy Awards ceremony since 1929. The organizers want to know how much it costs to organize such a ceremony.

Write a program that calculates the costs the academy will have to bear to organize the event, based on the rent for the hall where it will be held.

Cost Breakdown
Statuettes: The price is 30% less than the hall rent.
Catering: The price is 15% less than the cost of the statuettes.
Sound: The price is half of the cost for catering.
Input
One line is read from the console:

Rent for the hall: An integer in the range [0 ... 999].
Output
Print on the console the total cost of organizing the ceremony. The amount should be formatted to the second decimal place.

Example

Input:
500

Output:
1052.50

In this example, the rent for the hall is 500. The cost of the statuettes is 350 (30% less than the rent). The cost of catering is 297.50 (15% less than the statuette cost), and the cost of sound is 148.75 (half of the catering cost). The total cost of organizing the ceremony is 1296.25, which is formatted to two decimal places as 1052.50.



**Chalange 2. Shooting day**

You are the director of the movie "Programming is Fun" with a fixed time for shooting. You are asked to write a program that will tell you if you will have time to shoot the film on the day of shooting. The shooting day begins with field preparation, which is 15 percent of shooting time! A film has a certain number of scenes that are shot in a certain amount of time.

INPUT

3 lines are read from the console:

1. Snapshot time - an integer in the range [0… 1440]

2. Number of scenes - an integer in the range [5… 25]

3. Scene duration - an integer in the range [20… 90]

OUTPUT

To print one line to the console:

· If you run out of film time:

"You managed to finish the movie on time! You have {remaining time} minutes left!"

· If the time is NOT enough for YOU:

"Time is up! To complete the movie you need minutes."

Round the remaining time to the nearest whole number.


Example input and output

INPUT

120

10

11

OUTPUT

Time is up! To complete the movie you need 8 minutes.

INPUT
60

15

3

OUTPUT
You managed to finish the movie on time! You have 6 minutes left!