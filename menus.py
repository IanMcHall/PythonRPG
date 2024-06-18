from pick import pick
from enemies import *
from character_creator import *

# character_creation_menu = {
#     "1": "Warrior",
#     "2": "Paladin",
# }

battle_menu = {
    "1": "Attack",
    "2": "Assess",
    "3": "Status"
}

def battle_menu():
    title = "What will you do?"
    options = ["Attack", "Assess", "Status"]
    option, index = pick(options, title)
    
    if index == 0:
        print(f"\nYou attack the {first_enemy.name}!\n")
        if damage_done <= 0:
            damage_done = 1
        first_enemy.health -= damage_done
        print(f"The {first_enemy.name} takes {damage_done} damage!\n")
        if first_enemy.health <= 0:
            print("The enemy is defeated!")
            combat_active = False
            # break
        else:
            player_turn = False
    elif index == 1:
        print(f"\nYou assess the {first_enemy.name}\n")
        print(f"{first_enemy.name.capitalize()}: {first_enemy.bio}\n HP: {first_enemy.health}\n\n")
    elif index == 2:
        print(f"\nYou have {player_character.health} HP.\n")

battle_menu()
