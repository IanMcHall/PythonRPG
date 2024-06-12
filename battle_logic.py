from enemies import *
from character_creator import *
from menus import *
from battle_logic import *



def battle():
    damage_done = player_class.attack - current_enemy.defense
    damage_taken= current_enemy.attack - player_class.defense
    
    combat_active = current_enemy.health > 0 and player_class.health > 0
    player_turn = player_class.speed > current_enemy.speed 
    print(f"\nYou encounter a {current_enemy.name}!\n")
    if current_enemy.speed > player_class.speed:
        print(f"\nThe {current_enemy.name} has the upper hand!\n")
    while combat_active:
        
        if player_turn:
            print("What will you do?\n")
            for option_number, option in battle_menu.items():
                print(f"{option_number}. {option}")
            choice = input()

            while choice not in battle_menu:
                print("\nSelect a valid option\n")
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
                    combat_active = False
                    break
                else:
                    player_turn = False
                
            elif choice == "2":
                print(f"\nYou assess the {current_enemy.name}\n")
                print(f"{current_enemy.name.capitalize()}: {current_enemy.bio}\n HP: {current_enemy.health}\n\n")
            elif choice == "3":
                print(f"\nYou have {player_class.health} HP.\n")
            
        elif player_turn == False:
            print(f"\nThe {current_enemy.name} attacks!\n")
            if damage_taken <= 0:
                damage_taken = 1;
            player_class.health -= damage_taken;
            print(f"\nThe {current_enemy.name} hits you for {damage_taken} HP!\n")
            player_turn = True
            if player_class.health <= 0:
                print("The enemy defeats you...")
                combat_active = False
                break
            
battle()