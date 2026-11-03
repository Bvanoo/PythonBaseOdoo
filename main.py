import random
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

tab1 = [12, 5, 8]
tab2 = [3, 15, 2]

tailleTotale = len(tab1) + len(tab2)

tabFinal = [0] * tailleTotale
nbElements = 0

for element in tab1:
    i = nbElements - 1
    while i >= 0 and tabFinal[i] > element:
        tabFinal[i + 1] = tabFinal[i]
        i = i - 1
    tabFinal[i + 1] = element
    nbElements = nbElements + 1

for element in tab2:
    i = nbElements - 1
    while i >= 0 and tabFinal[i] > element:
        tabFinal[i + 1] = tabFinal[i]
        i = i - 1
    tabFinal[i + 1] = element
    nbElements = nbElements + 1

print("Tableau final trié (croissant) :", tabFinal)

tabFinal.reverse()
print("Tableau inversé (décroissant) :", tabFinal)

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
#             print("Limite droite atteinte !")
#
#     elif commande.lower() == "g":
#         if posPion > 0:
#             posPion = posPion - 1
#         else:
#             print("Limite gauche atteinte !")
#
#     elif commande.lower() == "q":
#         print("Fin du programme.")
#         continuer = False
#
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