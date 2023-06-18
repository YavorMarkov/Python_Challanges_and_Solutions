
[![Project Status: Under Construction](https://img.shields.io/badge/Project%20Status-Under%20Construction-yellow)](https://github.com/YavorMarkov/Python_Challanges_and_Solutions)


<i><sub>**NOTE**: This project is currently under construction. Please check back later for updates.</i></sub>



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

Snapshot time - an integer in the range [0… 1440]<br>
Number of scenes - an integer in the range [5… 25]<br>
Scene duration - an integer in the range [20… 90]

OUTPUT

To print one line to the console:

· If you run out of film time:<br>
"You managed to finish the movie on time! You have {remaining time} minutes left!"

· If the time is NOT enough for YOU:<br>
"Time is up! To complete the movie you need minutes."

Round the remaining time to the nearest whole number.

Example input and output

INPUT<br>
120<br>
10<br>
11<br>

OUTPUT<br>
Time is up! To complete the movie you need 8 minutes.<br>

INPUT<br>
60<br>
15<br>
3<br>


OUTPUT<br>
You managed to finish the movie on time! You have 6 minutes left!

**Task 3. Easter vacation**

During the Easter holidays, Desi wants to go on a vacation. The table shows the destinations and the price per night based on the dates she has booked the excursion.

Destinations – France , from 21-23 mart, price = 30 lv.
Destinations – France , from 24-27 mart, price = 35 lv.
Destinations – France , from 28-31 mart, price = 40 lv.

Destinations – Italy , from 21-23 mart, price = 28 lv.
Destinations – Italy , from 24-27 mart, price = 32 lv.
Destinations – Italy , from 28-31 mart, price = 39 lv.

Destinations – Germany , from 21-23 mart, price = 32 lv.
Destinations – Germany , from 21-23 mart, price = 37 lv.
Destinations – Germany , from 28-31 mart, price = 43 l

Write a program that calculates the cost of Desi's excursion, knowing the destination she wants to go to, the date she booked the excursion, and the number of nights she will stay in the given country.

Input
The input is read from the console and consists of three lines:
• First line - destination - a text with options "France", "Italy", or "Germany"
• Second line - booked excursion dates - text with options "21-23", "24-27", or "28-31"
• Third line - number of nights - an integer in the range [1… 100]
Output
The output should be printed on the console as a single line:
"Easter trip to {destination}: {excursion cost} leva."
The excursion cost should be formatted to the second decimal place.

Example Input and Output:<p>

INPUT:
Germany
24-27
5

OUTPUT:
Easter trip to Germany : 185.00 leva.

INPUT:
Italy
21-23
7

OUTPUT:
Easter trip to Italy : 196.00 leva.

INPUT:
France
28-31
8

OUTPUT:<r>
Easter trip to France : 320.00 leva.

