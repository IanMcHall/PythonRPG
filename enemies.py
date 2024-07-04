import random
from collections import Counter

class enemy:
    def __init__(self, name, health, attack, defense, speed, bio):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.bio = bio

    def __repr__(self):
        return f"Enemy({self.name}, health={self.health}, attack={self.attack}, defense={self.defense}, speed={self.speed})"

goblin = enemy("goblin", 6, 2, 1, 2, "Generic fantasy fodder.")
bearbug = enemy("bearbug", 2, 2, 3, 4, "A tiny, insect sized bear. Its ferocious growls reach your ears only as squeaks.")
bolder = enemy("bolder", 10, 3, 5, 1, "A particularly brave rock. It looks at you as if to say 'Who went and made you paper?'")
edgehog = enemy("edgehog", 8, 3, 3, 8, "The rootin-tootinist, fastest little critter you ever did see.")
#reaper is a test enemy and is too strong for gameplay
reaper = enemy("reaper", 100, 100, 100, 100, "There is no escape from death...")

enemy_dict = {
    "goblin": goblin,
    "bearbug": bearbug,
    "bolder": bolder,
    "edgehog": edgehog,
    "reaper": reaper
}

#current slection of enemies that are possible to encounter.
enemies = [goblin]
#bearbug, bolder, edgehog

first_enemy = random.choice(enemies)
second_enemy = random.choice(enemies)
third_enemy = random.choice(enemies)
fourth_enemy = random.choice(enemies)

def number_of_enemies():
    enemy_one = first_enemy.name
    enemy_two = second_enemy.name
    enemy_three = third_enemy.name
    enemy_four = fourth_enemy.name
    second_enemy_encounter =  False
    third_enemy_encounter =  False
    fourth_enemy_encounter =  False

    #determins number of enemies fought using RNG
    possible_current_enemies = [enemy_one]
    if random.choice([0,1]) > 0:
        possible_current_enemies.append(enemy_two)
        second_enemy_encounter = True
    if second_enemy_encounter and random.choice([0,3]) > 2:
            possible_current_enemies.append(enemy_three)
            third_enemy_encounter = True
    if third_enemy_encounter and random.choice([0,7]) > 6:
            possible_current_enemies.append(enemy_four)
            fourth_enemy_encounter = True
    
    
    enemy_count = Counter(possible_current_enemies)
    #if any isntance of an enemy is encountered more than once, the enemies are added to this dictionary, to be given a letter distinction
    #the enemy name is the key, and the value is always set to 0 by default.
    enemy_letter_count = {enemy: 0 for enemy in enemy_count if enemy_count[enemy] > 1}

    final_current_enemies = []

    for enemy in possible_current_enemies:
        if enemy in enemy_letter_count:
             enemy_letter_count[enemy] += 1
             #"chr(96)" is the final ASCII character before lowercase letters are introduced.
             #because an enemy type is only stored onced in the dictionary, each time it is iterated over -->
             #when there are multiple instances of the enemy, the value in the dictionary is increased by -->
             #one, then that value is converted to the appropriate letter.
             updated_name = f"{enemy} {chr(96 + enemy_letter_count[enemy])}"
             final_current_enemies.append(updated_name)
        else:
             final_current_enemies.append(enemy)

    final_enemies = []

    for name in final_current_enemies:
        if ' ' in name:
              base_name, letter = name.split(' ')
              final_enemies.append(enemy_dict[base_name])
        else:
             final_enemies.append(enemy_dict[name])
    return final_enemies
    #return final_current_enemies
    
final_enemies = number_of_enemies()
#inal_current_enemies = number_of_enemies()

#final_enemies = [enemy_dict[name] for name in final_current_enemies]

#enemies_by_speed = sorted(final_enemies, key=lambda enemy:enemy.speed, reverse=True)

for enemy in final_enemies:
     print(enemy.name)


