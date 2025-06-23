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
            break
        elif choice == "2":
            hero.heal()
            hero.health_bar.draw()
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

    hero.attack(enemy)
    hero.health_bar.draw()

    print("\n⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘\n")

    enemy.attack(hero)
    enemy.health_bar.draw()

    input()

    while hero.health > 0 and enemy.health > 0:
        # Player chooses action
        player_turn(hero, enemy)

        # Check if enemy is defeated
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")
            break

        # Enemy takes its turn
        enemy.take_turn(hero)

        # Check if hero is defeated
        if hero.health <= 0:
            print(f"{hero.name} has fallen!")
            break


    if hero.health <= 0:
        print(f"{hero.name} has fallen in battle!")
    elif enemy.health <= 0:
        print(f"{enemy.name} is defeated!")
        break