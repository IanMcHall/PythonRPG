#TODO
#Add critical hits, magic?, and items
#Change assessing enemy or checking player status not take take a turn.
#Add better documentation

#"import *" imports all data from the specified files. Classes, object instances, etc.
from enemies import *
from character_creator import *
from menus import *

#Calls the "character_creation function from the "character_creator.py file."
#Allows you to choose your class.
character_creation()

#battle logic
damage_done = player_class.attack - current_enemy.defense
damage_taken= current_enemy.attack - player_class.defense

#Battle loop

print(f"\nYou encounter a {current_enemy.name}!\n")



while current_enemy.health > 0 or player_class.health > 0:
    if player_class.speed > current_enemy.speed:
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
            continue
        elif choice == "3":
            print(f"\nYou have {player_class.health} HP.\n")
            continue
        print(f"\nThe {current_enemy.name} attacks!\n")
        if damage_taken <= 0:
            damage_taken = 1;
        player_class.health -= damage_taken;
        print(f"\nThe {current_enemy.name} hits you for {damage_taken} HP!\n")
        if player_class.health <= 0:
            print("The enemy defeats you...")
            break
    elif current_enemy.speed > player_class.speed:
        print(f"\nThe {current_enemy.name} attacks!\n")
        if damage_taken <= 0:
            damage_taken = 1;
        player_class.health -= damage_taken;
        print(f"\nThe {current_enemy.name} hits you for {damage_taken} HP!\n")
        if player_class.health <= 0:
            print("The enemy defeats you...")
            break
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
            continue
        elif choice == "3":
            print(f"\nYou have {player_class.health} HP.\n")
            continue

        