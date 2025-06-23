import random

# ------------ class setup ------------
class Weapon:
    def __init__(self,
                 name: str,
                 damage: int
                 ) -> None:
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"{self.name} (Damage: {self.damage})"

# ------------ object creation ------------
infectious_bite = Weapon("Infectious Bite", 3) # Ghoul

tackle_and_claws = Weapon("Tackle and Claws", 2) # Ghoul

bone_spear = Weapon("Bone Spear", 4) # Ghoul

false_life = Weapon("False Life", 5) # Necromancer

circle_of_death = Weapon("Circle of Death", 6) # Necromancer

inflict_wounds = Weapon("Inflict Wounds", 2) # Necromancer

paralysis = Weapon("Paralysis", 6) # Ghoul

necrotic_blast = Weapon("Necrotic Blast", 4) # Necromancer

bleeding_scream = Weapon("Bleeding Scream", 5) # Ghoul

ray_of_sickness = Weapon("Ray of Sickness", 3) # Necromancer

ghoul_weapons = [infectious_bite, tackle_and_claws, bone_spear, bleeding_scream, paralysis]
                
necro_weapons = [inflict_wounds, ray_of_sickness, necrotic_blast, false_life, circle_of_death]