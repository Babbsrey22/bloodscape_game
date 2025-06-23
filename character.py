from weapon import fists
from health_bar import HealthBar

import random


# ------------ parent class setup ------------
class Character:
    def __init__(self,
                 name: str,
                 health: int,
                 ) -> None:
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

    def attack(self, target) -> None:
        # Randomize damage between ±2 of the base weapon damage
        damage = random.randint(max(1, self.weapon.damage - 2), self.weapon.damage + 2)

        if random.random() < 0.1:  
            damage *= 2
            print("Critical hit!")

        target.health -= damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} dealt {damage} damage to {target.name} with {self.weapon.name}")


# ------------ subclass setup ------------
class Necromancer(Character):
    def __init__(self,
                 name: str,
                 health: int
                 ) -> None:
        super().__init__(name=name, health=health)

        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color="green")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon
    
    def heal(self):
        heal_amount = random.randint(5, 10)
        self.health = min(self.health + heal_amount, self.health_max)
        self.health_bar.update()
        print(f"{self.name} heals for {heal_amount} HP!")


# ------------ subclass setup ------------
class Ghoul(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon,
                 ) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon

        self.health_bar = HealthBar(self, color="yellow")
    
    def heal(self):
        heal_amount = random.randint(5, 10)
        self.health = min(self.health + heal_amount, self.health_max)
        self.health_bar.update()
        print(f"{self.name} heals for {heal_amount} HP!")

    def take_turn(self, target):
        # If ghoul health low, 50% chance to heal
        if self.health < self.health_max * 0.4 and random.random() < 0.5:
            self.heal()
            return
        
        if random.random() < 0.15:
            print(f"{self.name} tried to attack but missed!")
            return

        self.attack(target)