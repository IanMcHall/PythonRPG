import random

class enemy:
    def __init__(self, name, health, attack, defense, speed, bio):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.bio = bio

goblin = enemy("goblin", 6, 2, 1, 2, "Generic fantasy fodder.")
bearbug = enemy("bearbug", 2, 2, 3, 4, "A tiny, insect sized bear. Its ferocious growls reach your ears only as squeaks.")
bolder = enemy("bolder", 10, 3, 5, 1, "A particularly brave rock. It looks at you as if to say 'Who went and made you paper?'")
#reaper is a test enemy and is too strong for gameplay
reaper = enemy("reaper", 100, 100, 100, 100, "There is no escape from death...")

#current slection of enemies that are possible to encounter.
enemies = [goblin, bearbug]
current_enemy = random.choice(enemies)
second_enemy = random.choice(enemies)
third_enemy = random.choice(enemies)
fourth_enemy = random.choice(enemies)

def number_of_enemies():

    second_enemy_encounter =  None
    third_enemy_encounter =  None
    fourth_enemy_encounter =  None

    if random.choice([0,1]) > 0:
        second_enemy_encounter = True 
    if second_enemy_encounter and random.choice([0,3]) > 2:
            third_enemy_encounter = True
    if third_enemy_encounter and random.choice([0,7]) > 6:
            fourth_enemy_encounter = True
    
    # if current_enemy.name == second_enemy.name:
    #     current_enemy.name = current_enemy.name + " A"
    #     second_enemy.name = second_enemy.name + " B"
         
                
    print(current_enemy.name)
    if second_enemy_encounter == True:
        print(second_enemy.name)
    if third_enemy_encounter == True:
        print(third_enemy.name)
    if fourth_enemy_encounter == True:
        print(fourth_enemy.name)

number_of_enemies()