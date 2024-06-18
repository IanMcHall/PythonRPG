from menus import *
from pick import pick

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


#the player_character variable will be an instance of the player_characteres class
player_character = None

def character_creation():
    global player_character

    title = "Select your class"
    options = ["Warrior", "Paladin"]
    option, index = pick(options, title)
    
    if index == 0:
        player_character = warrior
    elif index == 1:
        player_character = paladin
    print(f"\nYou are a {player_character.class_name}.\n You have {player_character.health} HP, {player_character.attack} attack, and {player_character.defense} defense.\n")
character_creation()