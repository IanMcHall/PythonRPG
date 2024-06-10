import random

class enemy:
    def __init__(self, name, health, attack, defense, bio):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.bio = bio

goblin = enemy("goblin", 6, 2, 1, "Generic fantasy fodder.")
bearbug = enemy("bearbug", 2, 2, 4, "A tiny, insect sized bear. Its ferocious growls reach your ears only as squeaks.")
bolder = enemy("bolder", 10, 3, 5, "A particularly brave rock. It looks at you as if to say 'Who went and made you paper?'")
#reaper is a test enemy and is too strong for gameplay
reaper = enemy("reaper", 100, 100, 100, "There is no escape from death...")

enemies = [goblin, bearbug, bolder]
current_enemy = random.choice(enemies)