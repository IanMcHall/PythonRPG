class hero:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense

player_character = hero(10, 3, 2)

class enemy:
    def __init__(self, name, health, attack, defense, bio):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.bio = bio

goblin = enemy("goblin", 6, 2, 1, "Generic fantasy fodder.")
        

battle_menu = {
    "1": "Attack",
    "2": "Assess",
}



print(f"You encounter a {goblin.name}!\n")
print("What will you do?")
for option_number, option in battle_menu.items():
    print(f"{option_number}. {option}")
choice = input()
while choice not in battle_menu:
    choice = input("Select a valid option\n")
    