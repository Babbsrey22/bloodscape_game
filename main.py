# ------------ imports ------------
import os
import time

from instructions import Instructions
from character import Necromancer, Ghoul
from weapon import short_bow, iron_sword

# ------------ setup ------------
hero = Necromancer(name="Necromancer", health=100)
hero.equip(iron_sword)
enemy = Ghoul(name="Ghoul", health=100, weapon=short_bow)

def player_turn(hero, enemy):
    while True:
        print("\nYour Turn!")
        print("[1] Attack")
        print("[2] Heal")
        choice = input("Choose an action: ")

        if choice == "1":
            hero.attack(enemy)
            enemy.health_bar.update()
            enemy.health_bar.draw()
            hero.health_bar.draw()
            break
        elif choice == "2":
            hero.heal()
            hero.health_bar.draw()
            enemy.health_bar.draw()            
            break
        else:
            print("Invalid input. Please choose 1 or 2.")

# ------------ game loop ------------
while True:
    os.system("cls")

    print("" \
    " ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄   ██████  ▄████▄   ▄▄▄       ██▓███  ▓█████ \n" \
    "▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██░  ██▒▓█   ▀ \n" \
    "▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██░ ██▓▒▒███   \n" \
    "▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ \n" \
    "░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓ ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██▒ ░  ░░▒████▒\n" \
    "░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░\n" \
    "▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░▒ ░      ░ ░  ░\n" \
    " ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ ░  ░  ░  ░          ░   ▒   ░░          ░   \n" \
    " ░          ░  ░    ░ ░      ░ ░     ░          ░  ░ ░            ░  ░            ░  ░\n" \
    " ░                            ░               ░                                  ")

    Instructions()
    print("Press Enter to start"), input()

    while hero.health > 0 and enemy.health > 0:
        player_turn(hero, enemy)

        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")
            break

        enemy.take_turn(hero)

        if hero.health <= 0:
            print(f"{hero.name} has fallen!")
            break
