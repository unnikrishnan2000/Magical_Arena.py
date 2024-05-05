import random

class Player:
    def __init__(self, health, strength, attack):
        self.health = health
        self.strength = strength
        self.attack = attack

def roll_die():
    return random.randint(1, 6)

def fight(player1, player2):
    while player1.health > 0 and player2.health > 0:
        # Player with lower health attacks first
        if player1.health <= player2.health:
            attacker = player1
            defender = player2
        else:
            attacker = player2
            defender = player1

        # Attacker rolls the dice
        attack_roll = roll_die()
        attack_damage = attacker.attack * attack_roll

        # Defender rolls the dice
        defend_roll = roll_die()
        defend_damage = defender.strength * defend_roll

        # Calculate damage
        damage_taken = max(0, attack_damage - defend_damage)
        defender.health -= damage_taken

        # Switch roles for the next round
        player1, player2 = player2, player1

    if player1.health <= 0:
        return "Player 2 wins!"
    else:
        return "Player 1 wins!"

# Define players
playerA = Player(50, 5, 10)
playerB = Player(100, 10, 5)

# Simulate the fight
result = fight(playerA, playerB)
print(result)
