import time
import timeit
import random
from decimal import Decimal


# ======================================================================
# PARTIE 1 : CONDITIONS (if / elif / else)
# ======================================================================

# ----------------------------------------------------------------------
# 1.1 - Année bisextile
# ----------------------------------------------------------------------
"""
Demande une année à l'utilisateur et indique si elle est bissextile.
Règle : divisible par 4 ET non divisible par 100, OU divisible par 400.
Notions : modulo (%), opérateurs logiques (and / or).
"""
# year= int(input("Enter year: "))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Année bisextile")
# else:
#     print("Année non bisextile")


# ----------------------------------------------------------------------
# 1.2 - Lancer de balle (booléens prêt / panier vide)
# ----------------------------------------------------------------------
"""
Convertit deux saisies (0/1) en booléens et affiche un message selon
les 4 combinaisons possibles de "prêt" et "panier vide".
Notions : bool(int(input())), not, combinaison de conditions.
"""
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


# ----------------------------------------------------------------------
# 1.3 - Distributeur de boissons
# ----------------------------------------------------------------------
"""
L'utilisateur choisit une boisson (1 = coca, 2 = eau, 3 = fanta).
On vérifie le choix ET la présence de stock avant de servir.
Notions : if / elif avec condition composée, stock décrémenté.
"""
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


# ----------------------------------------------------------------------
# 1.4 - Calculatrice simple
# ----------------------------------------------------------------------
"""
Lit deux nombres et un opérateur (+ - * /), affiche le résultat.
Gère le cas particulier de la division par zéro et l'opérateur inconnu.
Notions : conversion int(), if imbriqués, f-strings.
"""
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


# ----------------------------------------------------------------------
# 1.5 - Mention selon la note
# ----------------------------------------------------------------------
"""
Convertit une note sur 20 en mention (Excellent, Très bien, Bien,
Suffisant, Échec) à l'aide de comparaisons chaînées (20 >= note >= 18).
"""
# note = int(input("Entrez votre note : "))
#
# if 20 >= note >= 18:
#     print("Excellent")
# elif 17 >= note >= 16:
#     print('Tres bien')
# elif 15 >= note >= 14:
#     print('bien')
# elif 13 >= note >= 12:
#     print('bien')
# elif 11 >= note >= 10:
#     print("Suffisant")
# elif 10 >= note >= 0:
#     print("Echec")
# else:
#     print("La note n'est pas valide")


# ======================================================================
# PARTIE 2 : BOUCLES (while / for)
# ======================================================================

# ----------------------------------------------------------------------
# 2.1 - Table de multiplication de 2
# ----------------------------------------------------------------------
"""
Affiche la table de 2 de 1 à 10 avec une boucle while et un compteur.
"""
# i=1
# while i <= 10 :
#     print(f" 2 * {i} = {2*i}")
#     i += 1


# ----------------------------------------------------------------------
# 2.2 - Lancer de balles avec un stock
# ----------------------------------------------------------------------
"""
Tant qu'il reste des balles et que le joueur est prêt, on lance
(Strike !) en décrémentant le stock. Après la boucle, on affiche la
raison de l'arrêt (pas prêt ou plus de balles).
Notions : while avec condition composée, drapeau booléen.
"""
# ready = bool(int(input("Ready ? y = 1 / n = o ")))
# stockBalle = int(input("Combien de balles dans le panier ?"))
# while stockBalle > 0 and ready:
#     print("Strike! ")
#     stockBalle -= 1
# if not ready:
#     print("U are not ready")
# elif stockBalle == 0 :
#     print("Aucune balle disponible")


# ----------------------------------------------------------------------
# 2.3 - Tables de multiplication de 2 à 10 (boucles imbriquées)
# ----------------------------------------------------------------------
"""
Affiche toutes les tables de 2 à 10. La boucle externe parcourt les
tables, la boucle interne les multiplicateurs de 1 à 10 (le compteur
interne est remis à 1 à chaque nouvelle table).
"""
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


# ----------------------------------------------------------------------
# 2.4 - Juste prix (deviner un nombre)
# ----------------------------------------------------------------------
"""
Tire un nombre aléatoire entre 1 et 100 et indique "trop haut" ou
"trop bas" jusqu'à ce que l'utilisateur trouve.
Attention : la saisie n'est pas redemandée dans la boucle, donc elle
tourne indéfiniment si le premier essai est faux (input à déplacer
dans le while).
"""
# randNum = random.randrange(1, 101)
# nbUser = int(input("Entrez un nombre entre 1 et 100: "))
# while nbUser != randNum:
#     if nbUser > randNum:
#         print("Trop haut")
#     elif nbUser < randNum:
#         print("Trop bas")
#     nbUser = int(input("Entrez un nombre entre 1 et 100: "))
# print(f"Félicitation le nombre étais {nbUser}")


# ======================================================================
# PARTIE 3 : TABLEAUX (listes)
# ======================================================================

# ----------------------------------------------------------------------
# 3.1 - Remplir une liste avec 6 saisies
# ----------------------------------------------------------------------
"""
Demande 6 valeurs à l'utilisateur et les stocke dans une liste avec
append(), en affichant le nombre de saisies restantes.
"""
# i = 1
# monTab = []
# while i <= 6:
#     monTab.append(int(input(f"Entrez une valeur, plus que {6-i} ")))
#     i+=1
# print(monTab)


# ----------------------------------------------------------------------
# 3.2 - Puissances de 2 jusqu'à 1024
# ----------------------------------------------------------------------
"""
Construit une liste des puissances de 2 (2, 4, 8 ... 1024) puis la
parcourt avec un index pour l'afficher élément par élément.
"""
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


# ----------------------------------------------------------------------
# 3.3 - Notes de joueurs : moyenne et affichage inversé
# ----------------------------------------------------------------------
"""
Saisie contrôlée du nombre de joueurs (1 à 10), puis d'une note par
joueur. Calcule la moyenne à la main et affiche la liste dans l'ordre
normal puis inversé avec le slicing [::-1].
"""
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


# ----------------------------------------------------------------------
# 3.4 - Tri à bulles
# ----------------------------------------------------------------------
"""
Trie une liste par ordre croissant avec le tri à bulles : on compare
les voisins et on les échange s'ils sont mal ordonnés, en réduisant la
zone parcourue à chaque passage. Comparé ensuite à la méthode native
sort().
"""
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


# ----------------------------------------------------------------------
# 3.5 - Fusion de deux listes en un tableau trié (tri par insertion)
# ----------------------------------------------------------------------
"""
Fusionne deux listes dans un tableau de taille fixe en insérant chaque
élément à sa bonne place (tri par insertion : on décale les plus grands
vers la droite). Affiche ensuite le résultat croissant puis décroissant
avec reverse().
"""
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


# ----------------------------------------------------------------------
# 3.6 - Parcours d'une liste à l'envers
# ----------------------------------------------------------------------
"""
Affiche les éléments d'une liste du dernier au premier avec
range(début, fin, pas) et un pas négatif.
"""
# tab = [5,10,42]
#
# for i in range(len(tab)-1,-1,-1):
#     print(tab[i])


# ----------------------------------------------------------------------
# 3.7 - Déplacement d'un pion sur un plateau
# ----------------------------------------------------------------------
"""
Un pion (1) se déplace sur un plateau de 10 cases (0). L'utilisateur
tape g / d / q pour aller à gauche, à droite ou quitter.
Notions : boucle while avec drapeau, gestion des bords du plateau.
"""
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


# ----------------------------------------------------------------------
# 3.8 - Recherche d'une valeur (arrêt au premier trouvé)
# ----------------------------------------------------------------------
"""
Recherche linéaire : parcourt la liste, mémorise l'index de la valeur
saisie et sort de la boucle avec break dès qu'elle est trouvée.
"""
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


# ----------------------------------------------------------------------
# 3.9 - Plus petit entier d'un tableau
# ----------------------------------------------------------------------
"""
Remplit un tableau de 10 entiers saisis, puis cherche le minimum à la
main : on part du premier élément et on garde le plus petit rencontré.
"""
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


# ----------------------------------------------------------------------
# 3.10 - Insertion d'une valeur dans un tableau trié
# ----------------------------------------------------------------------
"""
Insère une valeur saisie à sa place dans un tableau déjà trié, en
recopiant les éléments dans un nouveau tableau d'une case de plus
(deux index : i pour l'ancien tableau, j pour le nouveau).
"""
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


# ----------------------------------------------------------------------
# 3.11 - Recherche chronométrée (time.perf_counter)
# ----------------------------------------------------------------------
"""
Même recherche linéaire, mais sans break (parcourt tout le tableau) et
chronométrée avec time.perf_counter(). Le temps est affiché en
millisecondes.
"""
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


# ======================================================================
# PARTIE 4 : NOMBRES, FONCTIONS ET MESURE DE PERFORMANCE
# ======================================================================

# ----------------------------------------------------------------------
# 4.1 - Précision des nombres : Decimal vs float
# ----------------------------------------------------------------------
"""
Montre le piège des flottants : Decimal("0.3") (construit depuis une
chaîne) est exact, alors que Decimal(0.3) hérite de l'imprécision du
float 0.3. Comparer à 0.6 permet de voir la différence.
"""
# valeur = Decimal("0.3")
# valeurBis = Decimal(0.3)
# valeur2 = Decimal("0.3")
# valeur3 = Decimal(0.3)
#
# if valeur+valeur2 == 0.6:
#     print("Ca marche")
# if valeurBis+valeur3 == 0.6:
#     print("On me verras jamais")


# ----------------------------------------------------------------------
# 4.2 - Mesurer une fonction avec timeit
# ----------------------------------------------------------------------
"""
Définit une fonction carré et mesure son temps d'exécution avec
timeit. Sans l'argument number, timeit exécute la fonction 1 000 000
de fois.
"""
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


# ----------------------------------------------------------------------
# 4.3 - Fonction de recherche documentée + timeit
# ----------------------------------------------------------------------
"""
Fonction rechercher_element avec docstring : renvoie l'indice d'une
valeur dans un tableau, ou -1 si elle est absente. Testée sur deux
valeurs (présente / absente) et chronométrée.
"""
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


# ----------------------------------------------------------------------
# 4.4 - Fusion de listes : +, append, insert, extend
# ----------------------------------------------------------------------
"""
Compare plusieurs façons de manipuler des listes : append() ajoute à la
fin, insert() place à un index, "+" crée une nouvelle liste fusionnée
et extend() ajoute les éléments d'une liste à une autre (en place).
Les temps sont mesurés avec timeit puis perf_counter.
"""
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


# ======================================================================
# PARTIE 5 : DICTIONNAIRES, ENSEMBLES, CHAÎNES, FONCTIONS AVANCÉES
# ======================================================================

# ----------------------------------------------------------------------
# 5.1 - Dépaquetage des valeurs d'un dictionnaire
# ----------------------------------------------------------------------
"""
Utilise le dépaquetage étoilé (*reste) sur book.values() : isbn reçoit
la première valeur, dernier la dernière, et reste toutes celles du
milieu sous forme de liste.
"""
# test = "bonjour"
#
#
# book = {"isbn":"984855", "titre":"Petit prince", "prix":7.50,"bonjour":"hello","monde": "world"}
# isbn, *reste, dernier = book.values()
# print(reste)


# ----------------------------------------------------------------------
# 5.2 - Opérations sur les ensembles (set)
# ----------------------------------------------------------------------
"""
Différence entre deux ensembles (set_a - set_b : éléments de A qui ne
sont pas dans B), triée pour un affichage stable. Montre aussi la
création d'un dict et d'un set vides.
"""
# set_a = {"classique","sf"}
# set_b = {"thriller","western","sf"}
# print(sorted(set_a-set_b))
# dicti = dict()
# set_Test = set()


# ----------------------------------------------------------------------
# 5.3 - Chaînage de méthodes sur les chaînes
# ----------------------------------------------------------------------
"""
Nettoie et transforme un message : strip (espaces), lower (minuscules),
replace (remplacements), puis split + join pour changer le séparateur
en " | ".
"""
# msg = " Bonjour le monde "
# msg2 = msg.strip().lower().replace("le", "les").replace("monde", "odoo")
# print(msg2)
# messageTransformer = " | ".join(msg2.split(" "))
# print(messageTransformer)


# ----------------------------------------------------------------------
# 5.4 - Arguments nommés illimités (**kwargs)
# ----------------------------------------------------------------------
"""
Une fonction qui accepte un nombre quelconque d'arguments nommés,
récupérés sous forme de dictionnaire (**infos), puis parcourus avec
items().
"""
# def creer_profil(**infos):
#     for cle, valeur in infos.items():
#         print(f"{cle}: {valeur}")
#
# creer_profil(nom="Alice",
#              age=22,
#              ville="Lyon")


# ----------------------------------------------------------------------
# 5.5 - Filtrage par motifs (match / case)
# ----------------------------------------------------------------------
"""
Démonstration de match/case : cas littéral (1), cas avec garde
(capture + condition "if") et cas par défaut avec _.
"""
# choice = 1
#
# match choice :
#     case 1:
#         print("choix 1")
#     case choice_superieur_a_un if choice_superieur_a_un >1:
#         print("choix supérieur a 1")
#     case _:
#         print("Tout les choix non définis, peut etre n'importe quel caractère mais _ par convention")


# ----------------------------------------------------------------------
# 5.6 - Parcours d'une chaîne avec enumerate
# ----------------------------------------------------------------------
"""
Une chaîne est itérable : on la parcourt caractère par caractère, puis
avec enumerate() pour récupérer aussi l'index.
"""
# string_test = "hello"
# for i in string_test:
#     print(i)
# for i, v in enumerate(string_test):
#     print(f"index : {i} , Value: {v}")


# ======================================================================
# PARTIE 6 : EXERCICES COMPLETS
# ======================================================================

# ----------------------------------------------------------------------
# 6.1 - Jeu de Nim contre l'ordinateur
# ----------------------------------------------------------------------
"""
Jeu de Nim : on dispose de 13, 15 ou 16 bâtonnets (paramétrable), chaque
joueur en prend 1, 2 ou 3 par tour, celui qui prend le dernier gagne.
L'ordinateur est imbattable quand il joue la stratégie gagnante : il
laisse toujours un multiple de 4 à l'adversaire (prend batonnets % 4,
ou 1 s'il ne peut pas). Le joueur choisit qui commence ; les saisies
invalides sont refusées (try/except + vérification des bornes).
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


# ----------------------------------------------------------------------
# 6.2 - Palindromes : nettoyage et deux algorithmes comparés
# ----------------------------------------------------------------------
"""
Compter tous les palindromes uniques (mots complets, parties de mots,
phrase entière) de la phrase : "Ésope reste ici et se repose".

Étapes :
1. nettoyer_chaine : passe en minuscules, supprime les accents via un
   dictionnaire de correspondance et ne garde que les lettres.
2. palin (version compréhensions) : part des centres (paires de lettres
   identiques côte à côte, ou séparées par une lettre), puis étend tous
   les palindromes d'un cran à la fois en ne gardant que ceux dont les
   deux lettres voisines sont égales. Aucun slicing inutile.
3. all_palindrome_1 (version "Simon") : expansion depuis chaque centre
   avec une fonction palindrome() testant text[::-1] == text.
4. Les deux versions sont chronométrées avec timeit (number=1000) pour
   comparer leurs performances.
"""
# phrase = "Ésope reste ici et se repose"
#
# def nettoyer_chaine(texte):
#     correspondance = {
#         'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
#         'à': 'a', 'â': 'a', 'ä': 'a',
#         'î': 'i', 'ï': 'i',
#         'ô': 'o', 'ö': 'o',
#         'ù': 'u', 'û': 'u', 'ü': 'u',
#         'ç': 'c'
#     }
#     texte_minuscule = texte.lower()
#     return "".join(correspondance.get(c, c) for c in texte_minuscule if c.isalpha())
#
# texte_clean = nettoyer_chaine(phrase)
#
# def palin(txt):
#     n = len(txt)
#     niveau = (
#         [(i, i + 2) for i in range(n - 1) if txt[i] == txt[i + 1]]
#         + [(i, i + 3) for i in range(n - 2) if txt[i] == txt[i + 2]]
#     )
#
#     resultat = set()
#     while niveau:
#         resultat.update(txt[i:j] for i, j in niveau)
#         niveau = [(i - 1, j + 1) for i, j in niveau
#                   if i > 0 and j < n and txt[i - 1] == txt[j]]
#     return resultat
#
# res = palin(texte_clean)
# print(res, len(res))
#
# print(timeit.timeit(lambda: palin(texte_clean), number = 1000))


# Ancienne version en compréhension (force brute : teste toutes les sous-chaînes)
# def palin(txt):
#     palindromes = {
#         txt[i:j]
#         for i in range(len(txt))
#         for j in range(i + 2, len(txt) + 1)
#         if txt[i:j] == txt[i:j][::-1]
#     }
#     return palindromes
#
# print(f"Nombre de palindromes uniques trouvés : {len(palin(texte_clean))}")
# print("Liste :", sorted(palin(texte_clean), key=len, reverse=True))
#
# execPalin = timeit.timeit(lambda: palin(texte_clean))
# print(execPalin)

# def palindrome(text:str) -> bool:
#     if len(text) < 2:
#         return False
#     return text[::-1] == text
#
# def all_palindrome_1(text: str) -> int:
#
#     palindromes = set()
#
#     for index in range(len(text)):
#
#         check = True
#         reach = 1
#         while check and (index + reach) < len(text) and (index - reach) >= 0:
#             word = text[index - reach: index + reach + 1]
#             if palindrome(word):
#                 palindromes.add(word)
#                 reach += 1
#             else:
#                 check = False
#
#     for index in range(len(text) - 1):
#
#         check = True
#         reach = 0
#         while check and (index + reach) < len(text) and (index - reach) >= 0:
#             word = text[index - reach: index + 2 + reach]
#             if palindrome(word):
#                 palindromes.add(word)
#                 reach += 1
#             else:
#                 check = False
#
#     # print(palindromes)
#     return len(palindromes)
#
# execSimon = timeit.timeit(lambda: all_palindrome_1(texte_clean), number=1000)
# print(execSimon)


# ----------------------------------------------------------------------
# 6.3 - Compter les voyelles d'une phrase
# ----------------------------------------------------------------------
"""
Sur la même phrase que les palindromes, compte le nombre de voyelles
(a, e, i, o, u, y) du texte nettoyé avec sum() et un générateur.
"""
# nombre_voyelles = sum(
#     1 for c in nettoyer_chaine(phrase) if c in "aeiouy"
# )
# print(f"Nombre total de voyelles : {nombre_voyelles}")


# ----------------------------------------------------------------------
# 6.4 - Pyramide d'étoiles
# ----------------------------------------------------------------------
"""
Affiche une pyramide d'étoiles à partir d'un entier n : les lignes
montent de 1 à n étoiles puis redescendent jusqu'à 1.
Exemple : pyramide(3) → *, **, ***, **, *
Construit avec des compréhensions de liste, assemblées par "\\n".join.
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


# ----------------------------------------------------------------------
# 6.5 - Exo 26 de la banque : découpages valides
# ----------------------------------------------------------------------
"""
Étant donnée une suite de nombres, compte le nombre de façons de la
couper en deux parties non vides telles que la somme de la partie
gauche soit supérieure ou égale à celle de la partie droite.
Astuce : on calcule la somme totale une fois, puis on accumule la somme
de gauche ; la somme de droite vaut total - gauche (complexité O(n)).
Testé sur trois jeux de données avec timeit.
"""
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