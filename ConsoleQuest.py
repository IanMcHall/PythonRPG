#TODO
#Add enemy combat, losing player health, and lose conditon

from enemies import *
class hero:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense

player_character = hero(10, 3, 2)

battle_menu = {
    "1": "Attack",
    "2": "Assess",
}

damage_done = player_character.attack - current_enemy.defense

print(f"You encounter a {current_enemy.name}!\n")

while current_enemy.health > 0:
    print("What will you do?\n")
    for option_number, option in battle_menu.items():
        print(f"{option_number}. {option}")
    choice = input()

    while choice not in battle_menu:
        print("Select a valid option")
        for option_number, option in battle_menu.items():
            print(f"{option_number}. {option}")
            choice = input()
    if choice == "1":
        print(f"\nYou attack the {current_enemy.name}!\n")
        if damage_done <= 0:
            damage_done = 1
        current_enemy.health -= damage_done
        print(f"The {current_enemy.name} takes {damage_done} damage!\n")
        if current_enemy.health <= 0:
            print("The enemy is defeated!")
            break
    elif choice == "2":
        print(f"\nYou assess the {current_enemy.name}")
        print(" ")
        print(f"{current_enemy.name.capitalize()}: {current_enemy.bio}\n HP: {current_enemy.health}\n\n")
        



    