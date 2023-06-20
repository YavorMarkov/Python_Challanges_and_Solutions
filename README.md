[![Project Status: Under Construction](https://img.shields.io/badge/Project%20Status-Under%20Construction-yellow)](https://github.com/YavorMarkov/Python_Challanges_and_Solutions)

<div id="readme" style="display:none;">
 

<i><sub>**NOTE**: This project is currently under construction. Please check back later for updates.</i></sub>
# Heroes of Code and Logic VII

## Table of Contents

1. [Overview](#overview)
2. [Instructions](#instructions)
    1. [Hero Selection](#hero-selection)
    2. [Gameplay](#gameplay)
3. [Input](#input)
4. [Output](#output)
5. [Constraints](#constraints)
6. [Examples](#examples)

## Overview <a name="overview"></a>


You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic. You want to play it all day long! So cancel all other arrangements and create your party!

## Instructions <a name="instructions"></a>

### Hero Selection <a name="hero-selection"></a>

On the first line of the standard input, you will receive an integer `n` – the number of heroes that you can choose for your party. On the next `n` lines, the heroes themselves will follow with their hit points and mana points separated by a single space in the following format: 

{hero name} {HP} {MP}


- `HP` stands for hit points and `MP` for mana points
- a hero can have a maximum of 100 HP and 200 MP

### Gameplay <a name="gameplay"></a>

After you have successfully picked your heroes, you can start playing the game. You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given. 

There are several actions that the heroes can perform:

1. **CastSpell – {hero name} – {MP needed} – {spell name}**
2. **TakeDamage – {hero name} – {damage} – {attacker}**
3. **Recharge – {hero name} – {amount}**
4. **Heal – {hero name} – {amount}**

Each command has a specific effect and associated print message, as explained in the full problem statement.

## Input <a name="input"></a>

- On the first line of the standard input, you will receive an integer `n`
- On the following `n` lines, the heroes themselves will follow with their hit points and mana points separated by a space in the following format
- You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given

## Output <a name="output"></a>

- Print all members of your party who are still alive, sorted by their HP in descending order, then by their name in ascending order, in the following format (their HP/MP need to be indented 2 spaces):

{hero name}
HP: {current HP}
MP: {current MP}


## Constraints <a name="constraints"></a>

- The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative or exceed the respective limits.
- The HP/MP amounts in the commands will never be negative.
- The hero names in the commands will always be valid members of your party. No need to check that explicitly.

## Examples <a name="examples"></a>



| | |
|---|---|
| <span style="color: blue;">Input</span> | <pre>2<br>Solmyr 85 120<br>Kyrre 99 50<br>Heal - Solmyr - 10<br>Recharge - Solmyr - 50<br>TakeDamage - Kyrre - 66 - Orc<br>CastSpell - Kyrre - 15 - ViewEarth<br>End</pre> |
| <span style="color: green;">Output</span> | <pre>Solmyr healed for 10 HP!<br>Solmyr recharged for 50 MP!<br>Kyrre was hit for 66 HP by Orc and now has 33 HP left!<br>Kyrre has successfully cast ViewEarth and now has 35 MP!<br>Solmyr<br>&nbsp;&nbsp;HP: 95<br>&nbsp;&nbsp;MP: 170<br>Kyrre<br>&nbsp;&nbsp;HP: 33<br>&nbsp;&nbsp;MP: 35</pre> |

|  |  |
|---|---|
| **Input**  | <pre>4<br>Adela 90 150<br>SirMullich 70 40<br>Ivor 1 111<br>Tyris 94 61<br>Heal - SirMullich - 50<br>Recharge - Adela - 100<br>CastSpell - Tyris - 1000 - Fireball<br>TakeDamage - Tyris - 99 - Fireball<br>TakeDamage - Ivor - 3 - Mosquito<br>End</pre> |
| **Output**  | <pre>SirMullich healed for 30 HP!<br>Adela recharged for 50 MP!<br>Tyris does not have enough MP to cast Fireball!<br>Tyris has been killed by Fireball!<br>Ivor has been killed by Mosquito!<br>SirMullich<br>&nbsp;&nbsp;HP: 100<br>&nbsp;&nbsp;MP: 40<br>Adela<br>&nbsp;&nbsp;HP: 90<br>&nbsp;&nbsp;MP: 200</pre>  |


| **Comments** |
|---|
| <pre>Heal – SirMullich healed for 30 HP due to the HP max limit.<br>Recharge – Adela recharged for 50 MP due to the MP max limit.<br>CastSpell – Tyris does not have enough MP to cast the spell.<br>TakeDamage – Tyris's HP is reduced by 99, thus becoming -5, which means he is dead.<br>TakeDamage – Ivor's HP is now -2, so he is dead too.<br>After the "End" command, we print the remaining living heroes, sorted by their HP in reverse order.</pre> |

</div>
