import time
import timeit
import random
from decimal import Decimal

# year= int(input("Enter year: "))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Année bisextile")
# else:
#     print("Année non bisextile")

#
# ready = bool(int(input("Ready ? y = 1 / n = o ")))
# emptyBasket = bool(int(input("Empty Basket ? y  = 1 / n = o ")))
#
# if ready and not emptyBasket:
#     print("Strike! ")
# elif ready and emptyBasket:
#     print("No more ball!")
# elif not ready and not emptyBasket:
#     print("U are not ready ! ")
# else:
#     print("U are not ready and i've no more ball!")
#
# drink = int(input("Coca = 1 , Eau = 2 , Fanta = 3"))
# coca= 1
# eau = 0
# fanta = 2
# if drink == 1 and coca > 0:
#     print("Voici un coca")
#     coca -= 1
# elif drink == 2 and eau > 0:
#     print("Voici une eau")
# elif drink == 3 and fanta > 0:
#     print("Voici un fanta")
# else:
#     print("Choix incorrect où stock épuiser")

# nb1 = int(input("Nb1 : "))
# op = input("Choisissez un opérateur : ( + - * /")
# nb2 = int(input("Nb2 : "))
#
# if op == "+":
#     print(f"{nb1} + {nb2} = {nb1 + nb2}")
# elif op == "-":
#     print(f"{nb1} - {nb2} = {nb1 - nb2}")
# elif op == "*":
#     print(f"{nb1} * {nb2} = {nb1 * nb2}")
# elif op == "/":
#     if nb2 == 0:
#         print(f"On ne peut pas faire de division par 0")
#     else:
#         print(f"{nb1} / {nb2} = {nb1 / nb2}")
# else:
#     print("L'opérateur choisis ne fait pas partie de la liste ")

# note = int(input("Entrez votre note : "))
#
# if 20 >= note >= 18:
#     print("Excellent")
# elif 17 >= note >= 16:
#     print('Tres bien')
# elif 15 >= note >= 13:
#     print('bien')
# elif 14 >= note >= 12:
#     print('bien')
# elif 11 >= note >= 10:
#     print("Suffisant")
# elif 10 >= note >= 0:
#     print("Echec")
# else:
#     print("La note n'est pas valide")
#
# i=1
# while i <= 10 :
#     print(f" 2 * {i} = {2*i}")
#     i += 1
#
# ready = bool(int(input("Ready ? y = 1 / n = o ")))
# stockBalle = int(input("Combien de balles dans le panier ?"))
# while stockBalle > 0 and ready:
#     print("Strike! ")
#     stockBalle -= 1
# if not ready:
#     print("U are not ready")
# elif stockBalle == 0 :
#     print("Aucune balle disponible")
#
# i=2
# j=1
# while i <= 10 :
#     print(f"===== Table de {i} ======")
#     while j <= 10 :
#         print(f" {j} * {i} = {j*i}")
#         j+=1
#     print("=======================")
#     j = 1
#     i += 1
#
# randNum = random.randrange(1, 101)
# nbUser = int(input("Entrez un nombre entre 1 et 100: "))
# while nbUser != randNum:
#     if nbUser > randNum:
#         print("Trop haut")
#     elif nbUser < randNum:
#         print("Trop bas")
# print(f"Félicitation le nombre étais {nbUser}")

# i = 1
# monTab = []
# while i <= 6:
#     monTab.append(int(input(f"Entrez une valeur, plus que {6-i} ")))
#     i+=1
# print(monTab)

# j = 2
# monSuperTab = []
# while j <= 1024:
#     monSuperTab.append(j)
#     j *= 2
#
# j = 0
# while j < len(monSuperTab):
#     print(monSuperTab[j])
#     j+=1

# nbPlayer=int(input("Veuillez saisir le nombre de joueur: (max 10)"))
# while nbPlayer < 1 or nbPlayer > 10:
#     nbPlayer=int(input("Veuillez saisir un nombre entre 1 et 10"))
# noteJoueur = []
# for i in range(nbPlayer):
#     noteJoueur.append(int(input(f"Note du joueur n°{i+1}")))
# moy = 0
# for i in range(nbPlayer):
#     moy += noteJoueur[i]
# print(f"La moyenne des joueurs est de {moy/nbPlayer}")
#
# print(noteJoueur)
# print(noteJoueur[::-1])

#
# tab = [42, 10, 25, 18, 74, 108]
#
# n = len(tab)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if tab[j] > tab[j + 1]:
#             tab[j], tab[j + 1] = tab[j + 1], tab[j]
#
# print(tab)
# tab.sort()
# print(tab)

# tab1 = [12, 5, 8]
# tab2 = [3, 15, 2]
#
# tailleTotale = len(tab1) + len(tab2)
#
# tabFinal = [0] * tailleTotale
# nbElements = 0
#
# for element in tab1:
#     i = nbElements - 1
#     while i >= 0 and tabFinal[i] > element:
#         tabFinal[i + 1] = tabFinal[i]
#         i = i - 1
#     tabFinal[i + 1] = element
#     nbElements = nbElements + 1
#
# for element in tab2:
#     i = nbElements - 1
#     while i >= 0 and tabFinal[i] > element:
#         tabFinal[i + 1] = tabFinal[i]
#         i = i - 1
#     tabFinal[i + 1] = element
#     nbElements = nbElements + 1
#
# print("Tableau final trié (croissant) :", tabFinal)
#
# tabFinal.reverse()
# print("Tableau inversé (décroissant) :", tabFinal)
#

# tab = [5,10,42]
#
# for i in range(len(tab)-1,-1,-1):
#     print(tab[i])

# posPion = 0
# continuer = True
#
# while continuer:
#     plateau = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     plateau[posPion] = 1
#     print("Plateau actuel :", plateau)
#     commande = input("Deplacer (g = gauche, d = droite, q = quitter) : ")
#
#     if commande.lower() == "d":
#         if posPion < 9:
#             posPion = posPion + 1
#         else:
#             posPion = posPion % len(plateau)
#
#     elif commande.lower() == "g":
#         if posPion > 0:
#             posPion = posPion - 1
#         else:
#             posPion = posPion % len(plateau)-1
#
#     elif commande.lower() == "q":
#         print("Fin du programme.")
#         continuer = False
# #
#
# tab = [14, 25, 3, 42, 8, 19]
#
# valeurSaisie = int(input("Entrez la valeur à rechercher : "))
#
# position = -1
# trouve = False
#
# for i in range(len(tab)):
#     if tab[i] == valeurSaisie:
#         position = i
#         trouve = True
#         break
#
# if trouve:
#     print("La valeur", valeurSaisie, "se trouve à l'index :", position)
# else:
#     print("La valeur", valeurSaisie, "n'est pas dans le tableau.")

# tab = [0] * 10
#
# for i in range(len(tab)):
#     tab[i] = int(input("Entrez un entier : "))
#
# minimum = tab[0]
#
# for i in range(1, len(tab)):
#     if tab[i] < minimum:
#         minimum = tab[i]
#
# print("Le plus petit entier du tableau est :", minimum)
#
# tab = [2, 5, 8, 12, 15, 42]
# addInput = int(input("Entrez la valeur à insérer : "))
#
# tailleInitiale = len(tab)
# newTab = [0] * (tailleInitiale + 1)
#
# insere = False
# i = 0
# j = 0
#
# while i < tailleInitiale:
#     if not insere and addInput < tab[i]:
#         newTab[j] = addInput
#         j = j + 1
#         insere = True
#
#     newTab[j] = tab[i]
#     i = i + 1
#     j = j + 1
#
# if not insere:
#     newTab[j] = addInput
#
# print("Tableau après insertion :", newTab)
# import time
#
# tab = [12, 45, 7, 23, 89, 34]
# searchInput = int(input("Entrez la valeur à rechercher : "))
#
# debut = time.perf_counter()
#
# trouve = False
# position = -1
#
# for i in range(len(tab)):
#     if tab[i] == searchInput:
#         trouve = True
#         position = i
#
# if trouve:
#     print("La valeur", searchInput, "a été trouvée à la position (index) :", position)
# else:
#     print("La valeur", searchInput, "n'est pas dans le tableau.")
# fin = time.perf_counter()
# print(f"{(fin-debut)*1000:.6f}")

# valeur = Decimal("0.3")
# valeurBis = Decimal(0.3)
# valeur2 = Decimal("0.3")
# valeur3 = Decimal(0.3)
#
# if valeur+valeur2 == 0.6:
#     print("Ca marche")
# if valeurBis+valeur3 == 0.6:
#     print("On me verras jamais")


# test = 42
# t2 = 78
# t3=700
# t4=100
#
#
#
# def sqr(t):
#     return t*t
# execution = timeit.timeit(lambda:sqr(4)) # ⚠️ par défaut si on ne met pas de number il l'effectue 1 000 000 de fois
# print(sqr(4))
# print(f"{execution:6f}")

# def rechercher_element(tableau, taille, valeur_recherche):
#     """Recherche une valeur dans un tableau.
#     Renvoie l'indice de l'élément s'il existe, sinon -1.
#     """
#     for i in range(taille):
#         if tableau[i] == valeur_recherche:
#             return i
#     return -1
#
# notes = [12, 18, 5, 9, 15]
# taille_notes = len(notes)
#
# indice1 = rechercher_element(notes, taille_notes, 5)
# indice2 = rechercher_element(notes, taille_notes, 20)
#
# exec33 = timeit.timeit(lambda: rechercher_element(notes, taille_notes,5))
# print(exec33)
#
# print(f"Indice de 5 : {indice1}")
# print(f"Indice de 20 : {indice2}")
#
# tab = [0]*2
# tab.append(42)
# tab.insert(2,75)
# tab2 = [752,402,148]
#
# def mergeTab(tab1,tab2):
#     return tab+tab2
# print(mergeTab(tab,tab2))
# exec34 = timeit.timeit(lambda: mergeTab(tab,tab2))
# print(exec34)
#
# debut = time.perf_counter()
# tab.extend(tab2)
# fin = time.perf_counter()
# print(f"{(fin-debut)*1000:.6f}")

# test = "bonjour"
#
#
# book = {"isbn":"984855", "titre":"Petit prince", "prix":7.50,"bonjour":"hello","monde": "world"}
# isbn, *reste, dernier = book.values()
# print(reste)


# set_a = {"classique","sf"}
# set_b = {"thriller","western","sf"}
# print(sorted(set_a-set_b))
# dicti = dict()
# set_Test = set()


# msg = " Bonjour le monde "
# msg2 = msg.strip().lower().replace("le", "les").replace("monde", "odoo")
# print(msg2)
# messageTransformer = " | ".join(msg2.split(" "))
# print(messageTransformer)

# def creer_profil(**infos):
#     for cle, valeur in infos.items():
#         print(f"{cle}: {valeur}")
#
# creer_profil(nom="Alice",
#              age=22,
#              ville="Lyon")


# choice = 1
#
# match choice :
#     case 1:
#         print("choix 1")
#     case choice_superieur_a_un if choice_superieur_a_un >1:
#         print("choix supérieur a 1")
#     case _:
#         print("Tout les choix non définis, peut etre n'importe quel caractère mais _ par convention")

# string_test = "hello"
# for i in string_test:
#     print(i)
# for i, v in enumerate(string_test):
#     print(f"index : {i} , Value: {v}")

"""
Jeux de NYM, 13 ou 15 batonnets, les joueurs ont le droit d'en prendre 1 , 2 ou 3 par tour, celui qui prend le dernier a gagné. Faire de sorte de pouvoir jouer contre l'ordinateur, prévoir un algorithme qui ferais en sorte que l'ordinateur gange tout le temp
"""


# def jeu_nim(batonnets_depart=16):
#     batonnets = batonnets_depart
#     print(f"\n--- JEU DE NIM ({batonnets} bâtonnets) ---")
#
#     choix_depart = input("Qui commence ? (1 pour vous, 2 pour l'ordinateur) : ").strip()
#     tour_joueur = choix_depart != "2"
#
#     while batonnets > 0:
#         if tour_joueur:
#             try:
#                 choix_joueur = int(input(f"Il reste {batonnets} bâtonnets. Combien en prenez-vous (1, 2 ou 3) ? "))
#             except ValueError:
#                 print("Veuillez entrer un nombre valide (1, 2 ou 3).")
#                 continue
#
#             if choix_joueur not in [1, 2, 3] or choix_joueur > batonnets:
#                 print("Coup invalide ! Vous devez en prendre 1, 2 ou 3 (et pas plus que ce qu'il reste).")
#                 continue
#
#             batonnets -= choix_joueur
#             if batonnets == 0:
#                 print("Bravo, vous avez pris le dernier bâtonnet ! Vous avez gagné")
#                 break
#
#             tour_joueur = False
#         else:
#             reste = batonnets % 4
#             choix_ia = reste if reste != 0 else 1
#             batonnets -= choix_ia
#             print(f"L'ordinateur prend {choix_ia} bâtonnet(s). Il en reste {batonnets}.\n")
#
#             if batonnets == 0:
#                 print("L'ordinateur a pris le dernier bâtonnet. L'ordinateur a gagné")
#                 break
#
#             tour_joueur = True
# jeu_nim(15)

"""
Manipulation de string : ↓
"""

"""
Compter le nombre de palindrome présent dans la phrase : Ésope reste ici et se repose
Mot complet, partie de mot, phrase complète, tout les palindromes présent.
"""
phrase = "Ésope reste ici et se repose"

def nettoyer_chaine(texte):
    correspondance = {
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'à': 'a', 'â': 'a', 'ä': 'a',
        'î': 'i', 'ï': 'i',
        'ô': 'o', 'ö': 'o',
        'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c'
    }
    texte_minuscule = texte.lower()
    return "".join(correspondance.get(c, c) for c in texte_minuscule if c.isalpha())

texte_clean = nettoyer_chaine(phrase)

def palin(txt):
    palindromes = {
        txt[i:j]
        for i in range(len(txt))
        for j in range(i + 2, len(txt) + 1)
        if txt[i:j] == txt[i:j][::-1]
    }
    return palindromes

print(f"Nombre de palindromes uniques trouvés : {len(palin(texte_clean))}")
print("Liste :", sorted(palin(texte_clean), key=len, reverse=True))

execPalin = timeit.timeit(lambda: palin(texte_clean))
print(execPalin)

def palindrome(text:str) -> bool:
    if len(text) < 2:
        return False
    return text[::-1] == text

def all_palindrome_1(text: str) -> int:

    palindromes = set()

    for index in range(len(text)):

        check = True
        reach = 1
        while check and (index + reach) < len(text) and (index - reach) >= 0:
            word = text[index - reach: index + reach + 1]
            if palindrome(word):
                palindromes.add(word)
                reach += 1
            else:
                check = False

    for index in range(len(text) - 1):

        check = True
        reach = 0
        while check and (index + reach) < len(text) and (index - reach) >= 0:
            word = text[index - reach: index + 2 + reach]
            if palindrome(word):
                palindromes.add(word)
                reach += 1
            else:
                check = False

    # print(palindromes)
    return len(palindromes)

execSimon = timeit.timeit(lambda: all_palindrome_1(texte_clean))
print(execSimon)


"""
Sur la meme phrase que les palindrome, compter le nombre de voyelle
"""
# nombre_voyelles = sum(
#     1 for c in nettoyer_chaine(phrase) if c in "aeiouy"
# )
# print(f"Nombre total de voyelles : {nombre_voyelles}")
"""
Sur base de l'entrée de l'utilisateur, afficher une pyramide d' * 
pyramide(3) → *
              **
              ***
              **
              *
"""
# def pyramide(n):
#     niveaux = [i for i in range(1, n + 1)] + [i for i in range(n - 1, 0, -1)]
#     lignes = [f"* " * i for i in niveaux]
#     return "\n".join(lignes).strip()
#
#
# print(pyramide(5))
#
# execPyr = timeit.timeit(lambda:pyramide(5))
# print(execPyr)


"""Exo 26 de la banque"""
# def decoupages_valides(*nombres):
#     total = sum(nombres)
#     gauche = 0
#     valides = 0
#     for x in nombres[:-1]:
#         gauche += x
#         if gauche >= total - gauche:
#             valides += 1
#     return valides
#
# execDecoupage = timeit.timeit(lambda:decoupages_valides(10,4,-8,7))
# execDecoupageA = timeit.timeit(lambda:decoupages_valides(2,3,1,0))
# execDecoupageB = timeit.timeit(lambda:decoupages_valides(5))
# print(execDecoupage)
# print(execDecoupageA)
# print(execDecoupageB)
#










