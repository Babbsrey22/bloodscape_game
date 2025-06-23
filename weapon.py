# ------------ class setup ------------
class Weapon:
    def __init__(self,
                 name: str,
                 damage: int
                 ) -> None:
        self.name = name
        self.damage = damage


# ------------ object creation ------------
infectious_bite = Weapon(name = "Infectious Bite",
                    damage = 3) # Ghoul

tackle_and_claws = Weapon(name = "Tackle and Claws",
                damage = 2) # Ghoul

bone_spear = Weapon(name = "Bone Spear",
                    damage = 4) # Ghoul

false_life = Weapon(name = "False Life",
                    damage = 5) # Necromancer

circle_of_death = Weapon(name = "Circle of Death",
                         damage = 6) # Necromancer

inflict_wounds = Weapon(name = "Inflict Wounds",
                        damage = 2) # Necromancer

paralysis = Weapon(name = "Paralysis",
                   damage = 6) # Ghoul

necrotic_blast = Weapon(name = "Necrotic Blast",
                        damage = 4) # Necromancer

bleeding_scream = Weapon(name = "Bleeding Scream",
                         damage = 5) # Ghoul

ray_of_sickness = Weapon(name = "Ray of Sickness",
                         damage = 3) # Necromancer