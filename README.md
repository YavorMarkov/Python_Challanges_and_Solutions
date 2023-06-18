
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

**Challenge 3. Easter vacation**

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

**Challenge 4: Easter Eggs**



Easter is approaching, and one of the most exciting things is decorating Easter eggs. The available colors for painting the eggs are:
• Red
• Orange
• Blue
• Green

Write a program that calculates the number of eggs for each color and determines which color has the most eggs, given the total number of eggs and the color of each egg.

Input:
The input is read from the console and consists of the following:
• One line containing the total number of painted eggs (an integer in the range [1 ... 100])
For each egg, the following is read:
• The color of the egg - a text with options: "red", "orange", "blue", "green"

Output:
Print the following lines on the console:
• "Red eggs: {number of red eggs}"
• "Orange eggs: {number of orange eggs}"
• "Blue eggs: {number of blue eggs}"
• "Green eggs: {number of green eggs}"
• "Max eggs: {maximum number of eggs for a color} -> {color}"

Example Input and Output:

Input:
7
red
blue
green
red
orange
blue
green

Output:
Red eggs: 2
Orange eggs: 1
Blue eggs: 2
Green eggs: 2
Max eggs: 2 -> blue

Input:
12
red
red
red
orange
orange
blue
blue
blue
blue
green
green
green

Output:
Red eggs: 3
Orange eggs: 2
Blue eggs: 4
Green eggs: 3
Max eggs: 4 -> blue


**Challenge 5. Darts** 

Your task is to write a program that calculates whether a player has won a leg in a game of darts. (A leg refers to a single game of darts.)

Initially, the player starts with 301 points. The player throws the dart onto the dartboard, and for each hit, they score a certain number of points. Each field on the dartboard has three sectors: a Single sector, from which the points are taken as is, a Double sector, from which the points are doubled, and a Triple sector, from which the points are tripled.

The points obtained from each throw are subtracted from the initial points until reaching 0.

Note: If a throw results in more points than the remaining points, it is considered unsuccessful, and the player must throw again until they hit points equal to or less than the remaining points. Such a throw is considered successful.

Example: With 100 points remaining, a throw that results in more than 100 points is unsuccessful. With 100 points remaining, a throw that results in 100 points or fewer is successful.

Input:
The input consists of the following:

The player's name - text
Then, until the command "Retire" is received, the following two lines are read repeatedly:
Field - text ("Single", "Double", or "Triple")
Points - an integer in the range [0… 100]
Output:
The game ends when the command "Retire" is entered or when the initial 301 points are reduced to 0. The output should be a single line printed on the console:

If the player has won the leg:
"{player's name} won the leg with {successful throws} shots."
If the player has retired from the game:
"{player's name} retired after {unsuccessful throws} unsuccessful shots."
Example Input and Output

INPUT:<br>

Michael van Gerwen<br>
Triple<br>
20<br>
Triple<br>
19<br>
Double<br>
10<br>
Single<br>
3<br>
Single<br>
1<br>
Triple<br>
20<br>
Triple<br>
20<br>
Double<br>
20<br>

OUTPUT:<br>
Michael van Gerwen won the leg with 8 shots.

INPUT:<br>
Stephen Bunting<br>
Triple<br>
20<br>
Triple<br>
20<br>
Triple<br>
20<br>
Triple<br>
20<br>
Triple<br>
20<br>
Triple<br>
20<br>
Double<br>
7<br>
Single<br>
12<br>
Double<br>
1<br>
Single<br>
1<br>

OUTPUT:
Stephen Bunting won the leg with 6 shots.


INPUT:<br>
Rob Cross<br>
Triple<br>
20<br>
Triple<br>
20<br>
Triple<br>
20<br>
Triple<br>
20<br>
Double<br>
20<br>
Triple<br>
20<br>
Double<br>
5<br>
Triple<br>
10<br>
Double<br>
6<br>
Retire<br>


OUTPUT:<br>
Rob Cross retired after 3 unsuccessful shots.