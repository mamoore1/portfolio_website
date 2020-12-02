from math import floor
import random
from .generator_helper import ability_generator, dice_roller, mod_calculator, save_ratio
from .assign_ability_scores import assign_ability_score


# Defining a character class to hold the attributes we get from the CharClass model
# and the associated weapons lists. The final function will return a string representation
# of the character class
class Character:
    def __init__(self, char_class, level):
        self.level = level
        self.name = char_class.name
        self.hit_dice = char_class.hit_dice
        self.base_attack = char_class.base_attack
        self.fort_save_ratio = char_class.fort_save_ratio
        self.reflex_save_ratio = char_class.reflex_save_ratio
        self.will_save_ratio = char_class.will_save_ratio
        self.armour_proficiencies = char_class.armour_proficiencies.listedarmour_set.all()
        self.weapon_proficiencies = char_class.weapon_proficiencies.listedweapon_set.all()
        self.hp = 0
        self.str = 10
        self.str_mod = 0
        self.dex = 10
        self.con = 10
        self.int = 10
        self.wis = 10
        self.cha = 10
        self.fort_save = 0
        self.reflex_save = 0
        self.will_save = 0
        self.ac = 0
        self.extra_attacks = ''
        self.melee_attack = 0
        self.extra_melee_attacks = ''
        self.ranged_attack = 0
        self.extra_ranged_attacks = ''
        self.melee_weapon = ''
        self.ranged_weapon = ''
        self.armour = ''

    def __repr__(self):
        return f'''
        Level {self.level}
        {self.name} HP:{self.hp}  STR:{self.str} DEX:{self.dex} CON:{self.con} INT:{self.int} 
        WIS:{self.wis} CHA:{self.cha}
        F/R/W: +{self.fort_save}/+{self.reflex_save}/+{self.will_save}
        Base attack: +{self.base_attack}{self.extra_attacks}
        Melee attack: +{self.melee_attack}{self.extra_melee_attacks}
        Ranged attack: +{self.ranged_attack}{self.extra_ranged_attacks}
        Melee Weapon: {self.melee_weapon} Ranged Weapon: {self.ranged_weapon} Armour: {self.armour} AC:{self.ac}
        '''

    # A method which uses the character class's base attack and the characters level, str and dex to calculate
    # base attack, melee attack and ranged attack
    def update_attacks(self):
        base = self.base_attack
        level = self.level
        str_mod = mod_calculator(self.str)
        self.str_mod = str_mod
        dex_mod = mod_calculator(self.dex)
        self.base_attack = floor(base * level)
        self.melee_attack = self.base_attack + str_mod
        self.ranged_attack = self.base_attack + dex_mod

    def update_extra_attacks(self):
        base = self.base_attack
        melee = self.melee_attack
        ranged = self.ranged_attack
        num_bonus_attacks = floor((base-1)/5)  # First bonus attack at +6, second at +11 etc.
        self.extra_attacks = ''
        self.extra_melee_attacks = ''
        self.extra_ranged_attacks = ''
        for i in range(num_bonus_attacks):  # Each extra attack has an attack stat 5 lower than the previous attack
            self.extra_attacks += f'/+{base-(i+1)*5}'
            self.extra_melee_attacks += f'/+{melee-(i+1)*5}'  # Using "melee" and "ranged" rather than simply adding str or dex modifier
            self.extra_ranged_attacks += f'/+{ranged-(i+1)*5}'  # because melee and ranged might be updated based on magic weapons

    # A method which uses the character's save ratios, abilities and level to determine their saves.
    # This uses the "save_ratio" function defined in generator_helper
    def update_saves(self):
        level = self.level
        con_mod = mod_calculator(self.con)
        dex_mod = mod_calculator(self.dex)
        wis_mod = mod_calculator(self.wis)
        self.fort_save = save_ratio(self.fort_save_ratio, level) + con_mod
        self.reflex_save = save_ratio(self.reflex_save_ratio, level) + dex_mod
        self.will_save = save_ratio(self.will_save_ratio, level) + wis_mod

    def update_hp(self):
        con_mod = mod_calculator(self.con)
        hit_dice = self.hit_dice
        level = self.level
        self.hp = sum(dice_roller(level, con_mod, hit_dice))

    # Method which accesses the weapons through the weapon proficiency list and randomly assigns

    def select_weapons(self):
        weapon_list = self.weapon_proficiencies
        melee_weapons = []
        ranged_weapons = []
        for weapon in weapon_list:
            if weapon.weapon.weapon_mel_range == 0:
                melee_weapons.append(weapon.weapon)
            elif weapon.weapon.weapon_mel_range == 1:
                ranged_weapons.append(weapon.weapon)
        self.melee_weapon = random.choice(melee_weapons)
        self.ranged_weapon = random.choice(ranged_weapons)

    def select_armour(self):
        armour_list = self.armour_proficiencies
        try:
            self.armour = random.choice(armour_list).armour
        except IndexError:
            self.armour = None


    def update_ac(self):
        armour = self.armour
        dex_mod = mod_calculator(self.dex)
        if armour:
            armour_ac = armour.armour_ac
            if dex_mod > armour.armour_max_dex:
                dex_mod = armour.armour_max_dex
        else:
            armour_ac = 0
        self.ac = 10 + armour_ac + dex_mod


# A function which holds the other functions involved in generating the NPC
def character_generator(char_class, level):
    # Defining our character
    character = Character(char_class, level)
    ability_scores = ability_generator()
    assign_ability_score(character, char_class, ability_scores, level)
    character.update_attacks()
    character.update_saves()
    character.select_weapons()
    character.update_extra_attacks()
    character.update_hp()
    character.select_armour()
    character.update_ac()
    return character
