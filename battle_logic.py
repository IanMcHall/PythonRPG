from enemies import *
from character_creator import *
from menus import *
from common import player_character


def battle():
    damage_done = player_character.attack - first_enemy.defense
    damage_taken = first_enemy.attack - player_character.defense
    combat_active = first_enemy.health > 0 and player_character.health > 0
    battle_intro = first_enemy.health > 0 and player_character.health > 0
    player_turn = player_character.speed > first_enemy.speed
    
    def battle_menu():
        #nonlocal allows me to call variables outside of the scope of this function.
        nonlocal damage_done, combat_active, player_turn
        def enemy_selector():
            nonlocal player_turn

            title = "Select a target"
            options = final_current_enemies
            option,index = pick(options, title)

            if index == 0:
                print(f"\nYou attack the {first_enemy.name}!\n")
                if damage_done <= 0:
                    damage_done = 1
                first_enemy.health -= damage_done
                print(f"The {first_enemy.name} takes {damage_done} damage!\n")
                (input)
                if first_enemy.health <= 0:
                    print(f"{first_enemy.name} is defeated!")
                player_turn = False
            elif index == 1:
                print(f"\nYou attack the {second_enemy.name}!\n")
                if damage_done <= 0:
                    damage_done = 1
                second_enemy.health -= damage_done
                print(f"The {second_enemy.name} takes {damage_done} damage!\n")
                (input)
                if second_enemy.health <= 0:
                    print(f"{second_enemy.name} is defeated!")
                player_turn = False
            elif index == 2:
                print(f"\nYou attack the {third_enemy.name}!\n")
                if damage_done <= 0:
                    damage_done = 1
                third_enemy.health -= damage_done
                print(f"The {third_enemy.name} takes {damage_done} damage!\n")
                (input)
                if third_enemy.health <= 0:
                    print(f"{third_enemy.name} is defeated!")
                player_turn = False
            elif index == 3: 
                print(f"\nYou attack the {fourth_enemy.name}!\n")
                if damage_done <= 0:
                    damage_done = 1
                fourth_enemy.health -= damage_done
                print(f"The {fourth_enemy.name} takes {damage_done} damage!\n")
                (input)
                if fourth_enemy.health <= 0:
                    print(f"{fourth_enemy.name} is defeated!")
                player_turn = False
        
        title = "What will you do?"
        options = ["Attack", "Assess", "Status"]
        option, index = pick(options, title)
        
        if index == 0:
            enemy_selector()
        elif index == 1:
            print(f"\nYou assess the {first_enemy.name}\n")
            print(f"{first_enemy.name.capitalize()}: {first_enemy.bio}\n HP: {first_enemy.health}\n\n")
        elif index == 2:
            print(f"\nYou have {player_character.health} HP.\n")

    
    #displays at start of battle
    while battle_intro:
        for enemy in final_current_enemies:
            print(f"You encounter {enemy}!")
        input()
        battle_intro = False
        combat_active = True
        player_turn = True


    #There seems to be an issue where an enemy isn't removed from combat when killed. FIX.
    while combat_active:
        #player turn    
        if player_turn:
            battle_menu()
                
            print(f"\nThe {first_enemy.name} attacks!\n")
            input()
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
            
