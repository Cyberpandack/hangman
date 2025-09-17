import random

mots = ["pomme", "corsica", "magie","baguette"]
mot = random.choice(mots).upper()
trouvees = []
penalites = 0
max_penalites = 12

print(" Jeu du Pendu - Devine le mot !")

while penalites <= max_penalites:
    
    affichage = ' '.join([lettre if lettre in trouvees else '_' for lettre in mot])
    print(f"\n{affichage} / {penalites} pénalité(s)")

 
    entree = input(" Lettre ou mot entier : ").strip().upper()

    if len(entree) == 1 and entree.isalpha():
        if entree in mot:
            print(f"Bien joué ! La lettre '{entree}' est dans le mot.")
            if entree not in trouvees:
                trouvees.append(entree)
        else:
            print(f" Oups ! La lettre '{entree}' n'est pas dans le mot.")
            penalites += 1
    elif len(entree) == len(mot):
        if entree == mot:
            print(f" Bravo ! Tu as deviné le mot '{mot}' avec {penalites} pénalité(s).")
            break
        else:
            print(f" Mauvaise tentative pour le mot entier.")
            penalites += 5
    else:
        print(f" Entrée invalide. Tape une lettre ou tente le mot entier.")

    if all(lettre in trouvees for lettre in mot):
        print(f"\n Félicitations ! Tu as trouvé le mot '{mot}' avec {penalites} pénalité(s).")
        break

if penalites > max_penalites:
    print(f"\n Trop de pénalités ({penalites}). Le mot était '{mot}'. Game over.")
