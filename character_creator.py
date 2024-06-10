class player_classes:
    def __init__(self, class_name, health, attack, defense):
        self.class_name = class_name
        self.health = health
        self.attack = attack
        self.defense = defense


warrior = player_classes("warrior", 10, 4, 2)
paladin = player_classes("paladin", 10, 2, 4)

valid_classes = [warrior, paladin]

character_creation_menu = {
    "1": "Warrior",
    "2": "Paladin",
}

#the player_class variable will be an instance of the player_classes class
player_class = None

def character_creation():
    global player_class
    while player_class not in valid_classes:
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
            player_class = warrior
        elif choice == "2":
            player_class = paladin
        print(f"You are a {player_class.class_name}.\n You have {player_class.health} HP, {player_class.attack} attack, and {player_class.defense} defense.")
    
#DO NOT COMMENT OUT, WILL BREAK CALL ON MAIN FILE.
character_creation()