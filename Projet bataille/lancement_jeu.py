# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:16:48 2024

@author: MARION.THARREAU, EDWARD COURJAUD
"""

from class_carte import Carte
from class_joueur import Joueur
from class_main import Main
from class_paquet import Paquet
import random
 
def melanger_cartes(cartes):
    """
    Entrée : un tableau contenant les cartes
    Cette fonction mélange les valeurs d'un tableau
    Sortie : le tableau de cartes mélangées
    """
    return random.shuffle(cartes)


def valeur_carte(carte):
    """
    Entrée: une carte
    En creant un dictionnaire qui à pour objet le nom de la carte et pour 
    valeur la valeur numérique de la carte.
    Retourne la valeur numérique d'une carte.
    """
    valeurs = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10,
        'J': 11, 'Q': 12, 'K': 13, 'As': 14}
    return valeurs[carte.nombre]


def chercher_valeur(carte_joueur1,carte_joueur2):
    """
    entrée : la carte défilée du joueur 1 et celle du joueur2
    but : savoir quelle carte a la plus grande valeur
    sortie : appel de fonction gagner, perdre ou bataille
    """

    if valeur_carte(carte_joueur1) > valeur_carte(carte_joueur2):
        print('a')
        joueur1.gagner(carte_joueur1,carte_joueur2)
            
    elif valeur_carte(carte_joueur1) < valeur_carte(carte_joueur2):
        print('b')
        joueur2.gagner(carte_joueur1,carte_joueur2)
            
    elif valeur_carte(carte_joueur1) == valeur_carte(carte_joueur2):
        print('c')
        bataille(carte_joueur1,carte_joueur2)


tab_bataille=[]

def bataille(carte1,carte2):
    """
    retourne face cache et mettre dans un tableau quon enfilera dans la main du gagnant 
    retourne
    chercher_valeur()
    """
    tab_bataille.append(carte1)
    tab_bataille.append(carte2)
    print(tab_bataille)
   


# Création de variables

# Création des cartes
couleurs=['coeur','trèfle','carreaux','pique']
nombres=[2,3,4,5,6,7,8,9,10,'J','Q','K','As']
cartes=[]

for couleur in couleurs:
    for nombre in nombres:
        cartes+=[Carte(couleur,nombre)]

# Créations des tableaux contenants les cartes initiales des mains
jeu1=[]
jeu2=[]

# Création des mains des joueurs
main1=Main(jeu1)
main2=Main(jeu2)

# Création des joueurs
joueur1 = Joueur(main1, 'Joueur 1')
joueur2 = Joueur(main2, 'Joueur 2')

# Création des paquets
paquet=Paquet(cartes)
melanger_cartes(cartes)

# Distribution des cartes dans les tableaux des mains des joueurs
paquet.distribuer(jeu1,jeu2)


# Testes pour voir sir les mains des joueurs ont bien des cartes mélangées
print('Main du joueur 1 :')
for carte in joueur1.main.carte:
    print(carte.couleur, carte.nombre)
    
print('Main du joueur 2 :')
for carte in joueur2.main.carte:
    print(carte.couleur, carte.nombre)


# Boucle du jeu, début de la partie
game=True
while game:
    carte_joueur1 = joueur1.retourner_carte()
    carte_joueur2 = joueur2.retourner_carte()
    chercher_valeur(carte_joueur1,carte_joueur2)
    
    
    
    game=False
    
    









