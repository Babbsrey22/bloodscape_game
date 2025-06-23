# ------------ imports ------------
import os
import random
import time

from instructions import Instructions
from character import Necromancer, Ghoul
from weapon import ghoul_weapons
from dialogue_lines import necromancer_lines, victory_lines, defeat_lines

# ------------ setup ------------
hero = Necromancer(name="Necromancer", health=100)
enemy = Ghoul(name="Ghoul", health=100, weapon = random.choice(ghoul_weapons))
print(f"Necromancer starts with: {hero.weapon}")
print(f"The Ghoul starts with {enemy.weapon}")

def player_turn(hero, enemy):
    while True:
        print("\nYour Turn!")
        print("[1] Attack")
        print("[2] Heal")
        choice = input("Choose an action: ")

        if choice == "1":
            print(random.choice(necromancer_lines))
            hero.attack(enemy)
            time.sleep(0.5)
            hero.health_bar.draw()
            time.sleep(0.5)
            enemy.health_bar.update()
            enemy.health_bar.draw()
            break
        elif choice == "2":
            hero.heal()
            time.sleep(0.5)
            hero.health_bar.draw()
            time.sleep(0.5)
            enemy.health_bar.draw()            
            break
        else:
            print("Invalid input. Please choose 1 or 2.")

def repeat():
    while True:
        repeat = input("\nWould you like to start again? (y/n): ")
        if repeat.lower() == 'n':
            time.sleep(0.5)
            print("\n🕯️ The Necromancer fades into the shadows, his task unfinished...")
            print("☠ The dead will remember your choices.\n")
            print(1)
            print('''

▄▄▄█████▓ ██░ ██  ███▄    █  ██ ▄█▀  ██████      █████▒██▀███     ▄▄▄█████▓ ██░ ██     ███▄ ▄███▓ ███▄ ▄███▓ ██▀███    ██████ 
▓  ██▒ ▓▒▓██░ ██▒ ██ ▀█   █  ██▄█▒ ▒██    ▒    ▓██   ▒▓██ ▒ ██▒   ▓  ██▒ ▓▒▓██░ ██▒   ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓██ ▒ ██▒▒██    ▒ 
▒ ▓██░ ▒░▒██▀▀██░▓██  ▀█ ██▒▓███▄░ ░ ▓██▄      ▒████ ░▓██ ░▄█ ▒   ▒ ▓██░ ▒░▒██▀▀██░   ▓██    ▓██░▓██    ▓██░▓██ ░▄█ ▒░ ▓██▄   
░ ▓██▓ ░ ░▓█ ░██ ▓██▒  ▐▌██▒▓██ █▄   ▒   ██▒   ░▓█▒  ░▒██▀▀█▄     ░ ▓██▓ ░ ░▓█ ░██    ▒██    ▒██ ▒██    ▒██ ▒██▀▀█▄    ▒   ██▒
  ▒██▒ ░ ░▓█▒░██▓▒██░   ▓██░▒██▒ █▄▒██████▒▒   ░▒█░   ░██▓ ▒██▒     ▒██▒ ░ ░▓█▒░██▓   ▒██▒   ░██▒▒██▒   ░██▒░██▓ ▒██▒▒██████▒▒
  ▒ ░░    ▒ ░░▒░▒░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░    ▒ ░   ░ ▒▓ ░▒▓░     ▒ ░░    ▒ ░░▒░▒   ░ ▒░   ░  ░░ ▒░   ░  ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
    ░     ▒ ░▒░ ░░ ░░   ░ ▒░░ ░▒ ▒░░ ░▒  ░ ░    ░       ░▒ ░ ▒░       ░     ▒ ░▒░ ░   ░  ░      ░░  ░      ░  ░▒ ░ ▒░░ ░▒  ░ ░
  ░       ░  ░░ ░   ░   ░ ░ ░ ░░ ░ ░  ░  ░      ░ ░     ░░   ░      ░       ░  ░░ ░   ░      ░   ░      ░     ░░   ░ ░  ░  ░  
          ░  ░  ░         ░ ░  ░         ░               ░                  ░  ░  ░          ░          ░      ░           ░  
                                                                                                                              
                  ''')
            exit()
        elif repeat.lower() == 'y':
            time.sleep(0.5)
            print("\n𓌏 The Necromancer rises again... fate demands another battle.")
            print("⚰️ The crypt door creaks open once more.\n")
            break
        else:
            print("Choose 'y' or 'n' only.")

# ------------ game loop ------------
while True:
    os.system("cls")

    hero = Necromancer(name="Necromancer", health=100)
    enemy = Ghoul(name="Ghoul", health=100, weapon = random.choice(ghoul_weapons))

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
            time.sleep(1)
            print('''
                          ⠀⢀⣤⣀⠀⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⣤⣤⣤⣤⣤⣀ ⠀⠀⢀⣤⠚⠉⣨⣽⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⣤⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣶⠖⠋⣉⣩⣿⣿⡉⠀⠀ ⣾⣅⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⢀⡼⡿⢷⡲⢤⣉⢙⣳⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣾⣿⣿⣧⣶⣋⣡⡟⣸⡇⠙⠶  ⣻⣿⢻⣶⣿⣿⣿⣿⣿⣿⣻⣯⢿⣟⢀⣠⠾⢻⣄⣤⣤⡻⣴⣮⣙⢿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣴⡿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣈⠙⡒⠚⠳⡘⠛⠛⠿⢿⡿⠿⠛⠻⢿⠄⠀⣉⠁⣴⣿⣿⣿⣿⣿⣟⣿⣿⣶⣿⡟⠛⠛⠻⣧⡀⠀⠀⠀⠀⠀⠀
⡼⠋⠀⠀⠀⠉⠉⠉⠻⠿⠿⢿⣿⣿⣿⣿⡿⣿⠏⠁⠀⣿⣤⣠⡴⡾⢷⣤⣤⣤⣾⡃⠀⠉⠛⠻⣿⣿⣿⡿⠛⠉⠙⠁⠀⠀⠀⠀⠀⠀  ⠈⠓⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⠟⠁⠀⠀⠀⠺⡟⢻⣦⡍⠁⢀⠘⣷⡄⠛⠿⢿⠋⠀⠀⠀⠀⠙⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⢨⡈⠉⣷⣶⣭⣿⣿⣾⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠈⠻⠛⠟⠛⠈⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣾⣻⣿⣿⣿⣿⣟⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠚⠿⢿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ''')
            print(f"\t\t\t🪦{enemy.name} has been defeated!🪦\n")
            time.sleep(0.5)
            print(random.choice(victory_lines))
            repeat()
            break

        enemy.take_turn(hero)

        if hero.health <= 0:
            time.sleep(1)
            print('''
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO
       ::::::;       ;          OOOOO
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
                  ''')
            print(f"\t\t\t💀 {hero.name} has fallen.💀\n")
            time.sleep(0.5)
            print(random.choice(defeat_lines))
            repeat()
            break
