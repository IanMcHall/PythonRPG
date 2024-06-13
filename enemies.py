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
    enemy_one = current_enemy.name
    enemy_two = second_enemy.name
    enemy_three = third_enemy.name
    enemy_four = fourth_enemy.name
    second_enemy_encounter =  False
    third_enemy_encounter =  False
    fourth_enemy_encounter =  False

    if random.choice([0,1]) > 0:
        second_enemy_encounter = True
    if second_enemy_encounter and random.choice([0,3]) > 2:
            third_enemy_encounter = True
    if third_enemy_encounter and random.choice([0,7]) > 6:
            fourth_enemy_encounter = True
    


    if current_enemy.name == second_enemy.name:
        enemy_one = current_enemy.name + " a"
        enemy_two = second_enemy.name + " b"
    elif current_enemy.name != second_enemy.name:
         enemy_one = current_enemy.name
         enemy_two = second_enemy.name
    elif current_enemy.name == third_enemy.name:
        enemy_one = current_enemy.name + " a"
        enemy_three = third_enemy.name + " b"
    elif current_enemy.name == fourth_enemy.name:
        enemy_one = current_enemy.name + " a"
        enemy_four = fourth_enemy.name + " b" 
    if second_enemy.name == third_enemy.name and second_enemy.name != current_enemy.name:
        enemy_two = second_enemy.name + " a"
        enemy_three = third_enemy.name + " b"
    elif second_enemy.name == fourth_enemy.name and second_enemy.name != current_enemy.name:
         enemy_two = second_enemy.name + " a"
         enemy_four = fourth_enemy.name + " b"
    elif second_enemy.name == third_enemy.name:
         enemy_three = third_enemy.name + " c"
    
    if third_enemy.name != current_enemy.name and third_enemy.name != second_enemy.name:
        enemy_three = third_enemy.name
    elif third_enemy.name == current_enemy.name and third_enemy.name != second_enemy.name:
         enemy_one = current_enemy.name + " a"
         enemy_three = third_enemy.name + " b"
    elif  third_enemy.name != current_enemy.name and third_enemy.name != second_enemy.name and third_enemy.name == fourth_enemy.name:
         enemy_three = third_enemy.name + " a"
         enemy_four = fourth_enemy.name + " b"
    elif third_enemy.name == fourth_enemy.name and third_enemy.name != current_enemy.name:
        enemy_three = third_enemy.name + " b"
        enemy_four = fourth_enemy.name + " c"
    elif third_enemy.name == fourth_enemy.name and third_enemy.name:
         enemy_four = fourth_enemy.name + " d"
    elif third_enemy.name == current_enemy.name and third_enemy.name != second_enemy.name and third_enemy.name == fourth_enemy.name:
         enemy_one = current_enemy.name + " a"
         enemy_three = third_enemy.name + " b"
         enemy_four = fourth_enemy.name + " c"

         
         
    if second_enemy_encounter == True:            
        print(enemy_one)
        print(enemy_two)
    else:
         print(current_enemy.name)
    if third_enemy_encounter == True:
        print(enemy_three)
    if fourth_enemy_encounter == True:
        print(enemy_four)

number_of_enemies()