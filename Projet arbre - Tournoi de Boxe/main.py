# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:25:25 2024

@author: MARION.THARREAU, EDWARD COURJAUD
"""
from random import *
from arbre_objet import Noeud
from tkinter import *
from classement import classement_prov, reelclassement
#---------------------------------Création de l'arbre arbre----------------------------------#
#Création des Noeuds joueurs : ils ont en valeur leur nom si ils participent au tournoi ou None si ils ne participent pas
ines=Noeud('Ines','','')
gabin=Noeud('Gabin','','')
loane=Noeud('Loane','','')
cecile=Noeud('Cecile','','')
morgan=Noeud('Morgan','','')
emilie=Noeud('Emilie','','')
louna=Noeud('Louna','','')
anael=Noeud(('Anael'),'','')
arthur=Noeud('Arthur','','')
leah=Noeud('Leah','','')
jules=Noeud('Jules','','')
prune=Noeud('Prune','','')
maeva=Noeud(None,'','')
chloe=Noeud('Chloé','','')
ambre=Noeud(None,'','')
lea=Noeud('Léa','','')

joueurs=[ines, gabin, loane, cecile, morgan, emilie, louna, anael, arthur, leah, jules, prune, maeva, chloe, ambre, lea]
shuffle(joueurs)
nb_joueur=0
# Création de l'arbre, ayant 16 feuilles si il y a 9 joueurs ou plus, ou 8 feuilles si il y a 8 joueurs ou moins

#Connaitre le nombre de joueurs
for joueur in joueurs:
    if joueur.valeur is not None:
        nb_joueur+=1
        
#Création de l'arbre à 16 feuilles
if nb_joueur>8:
    rang3_1=Noeud(None,joueurs[0], joueurs[1])
    rang3_2=Noeud(None,joueurs[2], joueurs[3])
    rang3_3=Noeud(None, joueurs[4], joueurs[5])
    rang3_4=Noeud(None, joueurs[6], joueurs[7])
    rang3_5=Noeud(None, joueurs[8], joueurs[9])
    rang3_6=Noeud(None, joueurs[10], joueurs[11])
    rang3_7=Noeud(None, joueurs[12], joueurs[13])
    rang3_8=Noeud(None, joueurs[14], joueurs [15])

    rang2_1=Noeud(None, rang3_1, rang3_2)
    rang2_2=Noeud(None, rang3_3, rang3_4)
    rang2_3=Noeud(None, rang3_5, rang3_6)
    rang2_4=Noeud(None, rang3_7, rang3_8)
    
# ou création de l'arbre à 8 feuilles
elif nb_joueur<=8:
    nouv_joueurs=[Noeud(None,'',''),Noeud(None,'',''),Noeud(None,'',''),Noeud(None,'',''),Noeud(None,'',''),Noeud(None,'',''),Noeud(None,'',''),Noeud(None,'','')]
    liste_joueurs=[]
    for joueur in joueurs:
        if joueur.valeur is not None:
            liste_joueurs.append(joueur)
    for i, joueur in enumerate(liste_joueurs):
            nouv_joueurs[i]=joueur
    rang2_1=Noeud(None,nouv_joueurs[0], nouv_joueurs[4])
    rang2_2=Noeud(None,nouv_joueurs[1], nouv_joueurs[5])
    rang2_3=Noeud(None, nouv_joueurs[2], nouv_joueurs[6])
    rang2_4=Noeud(None, nouv_joueurs[3], nouv_joueurs[7])
    
rang1_1=Noeud(None, rang2_1, rang2_2)
rang1_2=Noeud(None, rang2_3, rang2_4)

vainqueur=Noeud(None, rang1_1, rang1_2)


#------------------------------------------------------------------------------#
def combat_boxe():
    '''
    Entrée : None
    But : faire un combat de box entre les deux joueurs
    Sortie : un entier : soit 0 (joueur 1 gagne) soit 1 (joueur 2 gagne)
    '''
    # Les deux joueurs commencent avec 50 points de vie
    pv_joueur1 = 100
    pv_joueur2 = 100
    
    while pv_joueur1 > 0 and pv_joueur2 > 0:  # Le combat continue tant qu'aucun joueur n'est à 0 pv
        # Le joueur attaquant est choisi au hasard
        attaquant = choice(['Joueur 1', 'Joueur 2'])
        degats = randint(5, 20)  # Les dégâts varient de 5 à 20
        
        if attaquant == 'Joueur 1':
            pv_joueur2 -= degats  # Joueur 1 attaque Bot2
        else:
            pv_joueur1 -= degats  # Joueur 2 attaque Bot1
        
    if pv_joueur1 > 0:
        return 1  # Joueur 1 gagne
    else:
        return 0  # Joueur 2 gagne


def duel(parent, fen, variable_pause, afficher_arbre,vainqueur, canvas, noeud, x, y, offset, bouton):
    '''
    Entrée : un parent (+ les varibales d'affichage)
    But : faire le duel entre les enfants du parent
    Sortie : None
    '''
    jeu=combat_boxe()
    if jeu == 0:
        parent.gagnant('gauche',fen,variable_pause, afficher_arbre,vainqueur, canvas, noeud, x, y, offset, bouton)
    else:
        parent.gagnant('droit',fen,variable_pause, afficher_arbre,vainqueur, canvas, noeud, x, y, offset, bouton)


def duel2(parent):
    #FONCTION POUR LE CLASSEMENT FINAL
    '''
    Entrée : un parent
    But : faire le duel entre les enfants du parent
    Sortie : None
    '''
    jeu=combat_boxe()
    if jeu == 0:
        parent.gagnant2('gauche')
    else:
        parent.gagnant2('droit')



def afficher_arbre(canvas, noeud, x, y, offset):
    """
    But : Fonction récursive pour afficher les nœuds et tracer les lignes sur le Canvas
    """

    if noeud is None:
        return

    # Rayon pour dessiner le cercle des nœuds
    rayon = 30

    # Dessiner le nœud comme un cercle avec du texte
    x1, y1 = x - rayon, y - rayon  # Coin supérieur gauche du cercle
    x2, y2 = x + rayon, y + rayon  # Coin inférieur droit du cercle
    canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black")
    #canvas.create_oval(x1, y1, x2, y2, fill="lightblue", outline="black")
    canvas.create_text(x, y, text=noeud.valeur, font=("Arial", 12, "bold"))

    # Calculer les positions des enfants (niveau suivant)
    next_y = y + 80  # Décalage vertical entre parent et enfants

    # Dessiner le sous-arbre gauche et tracer une ligne
    if noeud.gauche:
        next_x_gauche = x - offset  # Décalage horizontal pour le gauche
        canvas.create_line(x, y + rayon, next_x_gauche, next_y - rayon, arrow=FIRST)
        afficher_arbre(canvas, noeud.gauche, next_x_gauche, next_y, offset // 2)

    # Dessiner le sous-arbre droit et tracer une ligne
    if noeud.droit:
        next_x_droit = x + offset  # Décalage horizontal pour le droit
        canvas.create_line(x, y + rayon, next_x_droit, next_y - rayon, arrow=FIRST)
        afficher_arbre(canvas, noeud.droit, next_x_droit, next_y, offset // 2)
        


def bouton_clique(variable_pause):
    # Change la valeur de la variable pour arrêter l'attente (pour faire les combat après action du bouton)
    variable_pause.set(1)
    


def afficher_classement(classement_reel):
    '''
    Entrée : liste des joueurs classés
    But : Afficher le classement dans la fenêtre Tkinter
    Sortie : None
    '''
    fen = Tk()  
    fen.title("Classement Final")
    
    classement_text = "\n".join([f"{i+1}. {joueur}" for i, joueur in enumerate(classement_reel)])
    
    label_classement = Label(fen, text="Classement général après duels pour départager les ex-aequo:\n" + classement_text, font=("Arial", 12), justify=LEFT)
    label_classement.grid(row=1, column=1)  # Afficher en haut à gauche du cadre
    fen.mainloop()


def lancement():
    """
    Entrée: None
    But : Créer l'interface et lancer les fonctions pour faire le tournoi
    Sortie : un tableau 'classement_provisoire' qui représente le classement 
    des joueurs avant qu'il aient refait des duels'
    """
    fen = Tk()  
    fen.title("duel")
    
    Label(fen, text= 'Résultat du tournoi de boxe :', font=("Times New Roman", 20)).grid(row=0, column=0)
    # Création du canva qui contient l'arbre
    largeur = 1200
    hauteur = 450
    canvas_arbre = Canvas(fen, width=largeur, height=hauteur, bg="white")
    canvas_arbre.grid(row=1,column=0)
    
    # Point de départ pour la racine
    racine_x = largeur // 2  # Position horizontale (pour démarrer au centre)
    racine_y = 50            # Position verticale (niveau 0)
    offset = 300             # Décalage initial entre les feuilles
    
    # Variable Tkinter pour surveiller le changement
    variable_pause = IntVar(value=0)
 
    # Création du bouton pour lancer les duels
    bouton = Button(fen, text="Cliquez pour continuer", command=lambda:bouton_clique(variable_pause))
    bouton.grid(row=2, column=0, sticky='w')
    
    #lancement de la fonction principal qui gère les duels
    vainqueur.parcours(duel,fen,variable_pause, afficher_arbre,vainqueur, canvas_arbre, vainqueur, racine_x, racine_y, offset, bouton)
    afficher_arbre(canvas_arbre, vainqueur, racine_x, racine_y, offset)
    
    # Calcul du classement provisoire après les premiers duels
    classement_provisoire = classement_prov(vainqueur)
    print("Classement provisoire ( le premier est le dernier dans le tableau):", classement_provisoire, '\n')


    fen.mainloop()
    return classement_provisoire


#LANCEMENT DU TOURNOI
classement_provisoire=lancement()
print("Les joueurs refont des duels pour se départager les places !\n")
classement_reel=reelclassement(classement_provisoire, duel2)
afficher_classement(classement_reel)


