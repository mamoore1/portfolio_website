import random
from math import floor

# A function which takes in a Character, their class and assigns their ability scores
# accordingly.
def assign_ability_score(character, char_class, ability_scores, level=1):
    # defining dictionary which will allow us to translate primary abilities from char_class into text
    ability_dict = {1: 'str', 2: 'dex', 3: 'con', 4: 'int', 5: 'wis', 6: 'cha'}
    main_abilities = [char_class.primary_ability, char_class.secondary_ability, char_class.tertiary_ability]
    other_abilities = [] # Distinguishing between top three abilities and remaining abilities
    for i in range(1, 7):
        if i not in main_abilities:
            other_abilities.append(i)
    main_abilities = [ability_dict[num] for num in main_abilities] #Translating from numbers to text
    other_abilities = [ability_dict[num] for num in other_abilities]
    other_ability_scores = ability_scores[3:] # Separating out the other ability scores and randomising them
    random.shuffle(other_ability_scores)
    level_modifier = floor(level / 4)
    ability_scores[0] += level_modifier
    assigned_dict = { # Building a dictionary which assigns ability scores to their respective ability
        main_abilities[0]: ability_scores[0],
        main_abilities[1]: ability_scores[1],
        main_abilities[2]: ability_scores[2],
        other_abilities[0]: other_ability_scores[0],
        other_abilities[1]: other_ability_scores[1],
        other_abilities[2]: other_ability_scores[2]
    }
    character.str = assigned_dict['str']
    character.dex = assigned_dict['dex']
    character.con = assigned_dict['con']
    character.int = assigned_dict['int']
    character.wis = assigned_dict['wis']
    character.cha = assigned_dict['cha']
