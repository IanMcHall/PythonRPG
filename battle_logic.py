from enemies import *
from character_creator import *
from menus import *
from main import player_character




def battle():
    damage_done = player_character.attack - first_enemy.defense
    damage_taken = first_enemy.attack - player_character.defense
    combat_active = first_enemy.health > 0 and player_character.health > 0
    battle_start = first_enemy.health > 0 and player_character.health > 0
    player_turn = player_character.speed > first_enemy.speed

    # for enemy in number_of_enemies:
    #     print(f"You encounter {enemy.name}")
    
    #Remove this after "number_of_enemies" is implemented correctly
    second_enemy = False
    #displays at start of battle
    while battle_start: 
        if second_enemy == False:
            print(f"\nYou encounter a {first_enemy.name}!\n")
        if second_enemy == True and first_enemy.name == second_enemy.name:
            print(f"\nYou encounter {first_enemy.name}!\n")
            print(f"\nYou encounter {second_enemy.name}!\n")
        if third_enemy == True:
            print(f"\nYou encounter a {third_enemy.name}!\n")
        if fourth_enemy == True:
            print(f"\nYou encounter a {fourth_enemy.name}!\n")
        if first_enemy.speed > player_character.speed:
            print(f"\nThe {first_enemy.name} has the upper hand!\n")
        battle_start = False
    while combat_active:
        #player turn    
        if player_turn:
            battle_menu()
            print("\nWhat will you do?\n")
            for option_number, option in battle_menu.items():
                print(f"{option_number}. {option}")
            choice = input()

            while choice not in battle_menu:
                print("\nSelect a valid option\n")
                for option_number, option in battle_menu.items():
                    print(f"{option_number}. {option}")
                choice = input()
            if choice == "1":
                print(f"\nYou attack the {first_enemy.name}!\n")
                if damage_done <= 0:
                    damage_done = 1
                first_enemy.health -= damage_done
                print(f"The {first_enemy.name} takes {damage_done} damage!\n")
                if first_enemy.health <= 0:
                    print("The enemy is defeated!")
                    combat_active = False
                    break
                else:
                    player_turn = False
                
            elif choice == "2":
                print(f"\nYou assess the {first_enemy.name}\n")
                print(f"{first_enemy.name.capitalize()}: {first_enemy.bio}\n HP: {first_enemy.health}\n\n")
            elif choice == "3":
                print(f"\nYou have {player_character.health} HP.\n")
        #enemy turn   
        elif player_turn == False:
            print(f"\nThe {first_enemy.name} attacks!\n")
            if damage_taken <= 0:
                damage_taken = 1;
            player_character.health -= damage_taken;
            print(f"\nThe {first_enemy.name} hits you for {damage_taken} HP!\n")
            player_turn = True
            if player_character.health <= 0:
                print("The enemy defeats you...")
                combat_active = False
                break
battle()
            
