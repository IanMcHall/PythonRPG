#TODO
#Add critical hits, magic?, and items
#Change assessing enemy or checking player status not take take a turn.
#Implement multiple enemies to single battle.
#Add better documentation

#To play, run this file.

#"import *" imports all data from the specified files. Classes, object instances, etc.
from enemies import *
from character_creator import *
from menus import *
from battle_logic import *

#Calls the "character_creation function from the "character_creator.py file."
#Allows you to choose your class.
character_creation()
#Calls the "battle()" function from the "battle_logic.py" file. 
#Initiates and carries out a fight with an enemy.
battle()
