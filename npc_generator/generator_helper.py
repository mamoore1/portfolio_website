# A set of functions that will be used when generating characters
from numpy import array
from random import choices
from math import floor

# A function which carries out dice rolls
def dice_roller(dice=1, modifier=0, sides=6):
    result = array(choices(range(1, sides+1), k=dice))
    result += modifier
    return result


# Function for rolling four d6 and dropping the lowest, used to generate ability scores
def fourd6drop1():
    result = dice_roller(dice=4)
    result.sort()
    result = result[1:4]
    return sum(result)


# Function for generating a sorted list of ability scores
def ability_generator():
    ability_list = []
    for i in range(6):
        ability_list.append(fourd6drop1())
    ability_list.sort(reverse=True)
    return ability_list

# Function to generate the modifier score (bonus or penalty) for a given ability
def mod_calculator(ability):
    return floor((ability-10)/2)

# Function which takes in a description of the char_class's save ratio and the character's level and determines their base save
def save_ratio(ratio, level):
    if ratio == 'poor':
        return floor(level * (1/3))
    elif ratio == 'good':
        return 2 + floor(level * 0.5)
    else:
        print('WTF')