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

goblin_damage_done = goblin.health + goblin.defense - player_character.attack 

print(f"You encounter a {goblin.name}!\n")

while goblin.health > 0:


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
        print(f"\nYou attack the {goblin.name}!\n")
        goblin.health -= goblin_damage_done
        print(f"The {goblin.name} takes {goblin_damage_done} damage!\n")
        if goblin.health <= 0:
            print("The enemy is defeated!")
            break
    elif choice == "2":
        print(f"\nYou assess the {goblin.name}")
        print(" ")
        print(f"{goblin.name.capitalize()}: {goblin.bio}\n HP: {goblin.health}\n\n")
        



    