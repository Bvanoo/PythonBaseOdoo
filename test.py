import msvcrt
import subprocess

taille_plateau = 10
pos_pion = 0
continuer = True

while continuer:
    subprocess.run("cls", shell=True)

    plateau = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    plateau[pos_pion] = "P"

    print("=== DEPLACEMENT DU PION (MODULO) ===")
    print("Plateau :", plateau)
    print("Commandes : [g]auche | [d]roite | [q]uitter")
    print("\n(Appuyez directement sur une touche...)")

    touche = msvcrt.getch().decode("latin1").lower()

    if touche == "d":
        pos_pion = (pos_pion + 1) % taille_plateau

    elif touche == "g":
        pos_pion = (pos_pion - 1) % taille_plateau

    elif touche == "q":
        print("\nFin du programme.")
        continuer = False