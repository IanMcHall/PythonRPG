from menus import *

class player_classes:
    def __init__(self, class_name, health, attack, defense, speed):
        self.class_name = class_name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed


warrior = player_classes("warrior", 10, 4, 2, 3)
paladin = player_classes("paladin", 10, 2, 4, 3)

valid_classes = [warrior, paladin]



#the player_class variable will be an instance of the player_characteres class
player_character = None

def character_creation():
    global player_character
    while player_character not in valid_classes:
        print("Select your class:")
        for option_number, option in character_creation_menu.items():
            print(f"{option_number}. {option}")
        choice = input()

        while choice not in character_creation_menu:
            print("Select a valid option")
            for option_number, option in character_creation_menu.items():
                print(f"{option_number}. {option}")
            choice = input()

        if choice == "1":
            player_character = warrior
        elif choice == "2":
            player_character = paladin
        print(f"\nYou are a {player_character.class_name}.\n You have {player_character.health} HP, {player_character.attack} attack, and {player_character.defense} defense.\n")
    
#DO NOT COMMENT OUT, WILL BREAK CALL ON MAIN FILE.
character_creation()