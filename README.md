[![Project Status: Under Construction](https://img.shields.io/badge/Project%20Status-Under%20Construction-yellow)](https://github.com/YavorMarkov/Python_Challanges_and_Solutions)


<i><sub>**NOTE**: This project is currently under construction. Please check back later for updates.</i></sub>

# Heroes of Code and Logic VII

## Table of Contents
1. [Introduction](#introduction)
2. [Gameplay](#gameplay)
3. [Input](#input)
4. [Output](#output)
5. [Constraints](#constraints)


<a name="introduction"></a>
## Introduction
This is a project for the Heroes of Code and Logic VII game. The game is the most recent update on the best MMORPG of all time.

<a name="gameplay"></a>
## Gameplay
Detailed gameplay instructions and rules can be found [here](link to instructions file or section)

<a name="input"></a>
## Input
* On the first line of the standard input, you will receive an integer n
* On the following n lines, the heroes themselves will follow with their hit points and mana points separated by a space in the following format
* You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given

<a name="output"></a>
## Output
* Print all members of your party who are still alive, sorted by their HP in descending order, then by their name in ascending order, in the following format (their HP/MP need to be indented 2 spaces): "{hero name}\n  HP: {current HP}\n  MP: {current MP}"

<a name="constraints"></a>
## Constraints
* The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative or exceed the respective limits.
* The HP/MP amounts in the commands will never be negative.
* The hero names in the commands will always be valid members of your party. No need to check that explicitly.


## Examples

| | |
|---|---|
| Input | <pre>2<br>Solmyr 85 120<br>Kyrre 99 50<br>Heal - Solmyr - 10<br>Recharge - Solmyr - 50<br>TakeDamage - Kyrre - 66 - Orc<br>CastSpell - Kyrre - 15 - ViewEarth<br>End</pre> |
| Output | <pre>Solmyr healed for 10 HP!<br>Solmyr recharged for 50 MP!<br>Kyrre was hit for 66 HP by Orc and now has 33 HP left!<br>Kyrre has successfully cast ViewEarth and now has 35 MP!<br>Solmyr<br>&nbsp;&nbsp;HP: 95<br>&nbsp;&nbsp;MP: 170<br>Kyrre<br>&nbsp;&nbsp;HP: 33<br>&nbsp;&nbsp;MP: 35</pre> |
