# Magical_Arena.py
This Python code simulates a simple turn-based fight between two players represented by the Player class. Let's break down the code step by step:

Player Class:
The Player class is defined with three attributes: health, strength, and attack.
When creating a new player object, you provide values for these attributes.
roll_die() Function:
This function simulates rolling a six-sided die (1 to 6) and returns the result.
It uses the random.randint() function from the random module to generate a random integer within the specified range.
fight() Function:
This function simulates the fight between two players.
It takes two player objects (player1 and player2) as parameters.
The fight continues in rounds until one of the players' health drops to 0 or below.
In each round, the player with lower health attacks first.
The attacker rolls a die to determine the attack strength (attack_roll) and calculates the damage inflicted (attack_damage).
The defender rolls a die to determine the defense strength (defend_roll) and calculates the damage mitigated (defend_damage).
The actual damage taken by the defender is calculated by subtracting the defense from the attack (damage_taken).
After each round, the roles of attacker and defender are switched.
The function returns a string indicating which player wins the fight.
Main Code:
Two player objects (playerA and playerB) are instantiated with their respective health, strength, and attack values.
The fight() function is called with these player objects, and the result is printed.
