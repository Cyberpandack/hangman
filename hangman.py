
import threading
import random
from english_words import get_english_words_set
import time
import sys

mots = list(get_english_words_set(['web2'], lower=True))
mots = [mot.upper() for mot in mots if 0 <= len(mot) <= 8]
mot = random.choice(mots)

trouvees = []
penalites = 0
max_penalites = 12

temps_max = 300
def countdown(temps):
    while temps > 0:
        m, s = divmod(temps, 60)
        print(f"\r,\t \t \t \t \t \t {m:02d}:{s:02d}", end='')
        time.sleep(1)
        temps -= 1
    print(f"\n 00:00 Temps écoulé !")
    exit()

timer_thread = threading.Thread(target=countdown, args=(temps_max,))
timer_thread.daemon = True
timer_thread.start()


print("\nJeu du Pendu - Devine le mot !")

while penalites <= max_penalites:
    affichage = ' '.join([lettre if lettre in trouvees else '_' for lettre in mot])
    print(f"\n{affichage} / {penalites} pénalité(s)")

    entree = input("Lettre ou mot entier : ").strip().upper()

    if len(entree) == 1 and entree.isalpha():
        if entree in mot:
            if entree not in trouvees:
                trouvees.append(entree)
            print(f"Bien joué ! La lettre '{entree}' est dans le mot.")
        else:
            penalites += 1
            print(f"Oups ! La lettre '{entree}' n'est pas dans le mot.")
    elif len(entree) == len(mot):
        if entree == mot:
            print(f"\nBravo ! Tu as deviné le mot '{mot}' avec {penalites} pénalité(s).")
            break
        else:
            penalites += 5
            print("Mauvaise tentative pour le mot entier.")
    else:
        print("Entrée invalide. Tape une lettre ou tente le mot entier.")

    if all(lettre in trouvees for lettre in mot):
        print(f"\nFélicitations ! Tu as trouvé le mot '{mot}' avec {penalites} pénalité(s).")
        break

else:
    print(f"\nTrop de pénalités ({penalites}). Le mot était '{mot}'. Game over.")
