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
infectious_bite = Weapon("Infectious Bite", 5) # Ghoul

tackle_and_claws = Weapon("Tackle and Claws", 4) # Ghoul

bone_spear = Weapon("Bone Spear", 6) # Ghoul

false_life = Weapon("False Life", 7) # Necromancer

circle_of_death = Weapon("Circle of Death", 8) # Necromancer

inflict_wounds = Weapon("Inflict Wounds", 4) # Necromancer

paralysis = Weapon("Paralysis", 8) # Ghoul

necrotic_blast = Weapon("Necrotic Blast", 6) # Necromancer

bleeding_scream = Weapon("Bleeding Scream", 7) # Ghoul

ray_of_sickness = Weapon("Ray of Sickness", 5) # Necromancer

ghoul_weapons = [infectious_bite, tackle_and_claws, bone_spear, bleeding_scream, paralysis]
                
necro_weapons = [inflict_wounds, ray_of_sickness, necrotic_blast, false_life, circle_of_death]