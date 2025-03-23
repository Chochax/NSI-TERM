# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:23:21 2025

@author: EDOUARD.COURJAUD
"""
from random import *
from arbre_objet import Noeud

def construire_arbre(joueurs):
    """
    Entrée : un tableau contenant des noeuds qui sont les joueurs feuille de notre arbre
    But : créer l'arbre avec ces feuilles
    Sortie : l'arbre créé
    """

    if not joueurs:
        return None
    if len(joueurs) == 1:  # Feuille
        return Noeud(joueurs[0])
    milieu = len(joueurs) // 2
    gauche = construire_arbre(joueurs[:milieu])  # Partie gauche
    droit = construire_arbre(joueurs[milieu:])   # Partie droite
    return Noeud(None, gauche, droit)


def classement_prov(arbre):
    '''
    Entrée : une racine
    But : Générer le classement provisoire avant départage des ex-aequo
    Sortie : Une liste des joueurs classés par rang
    '''
    classement_provisoire = []
    
    def parcours_provisoire(noeud, niveau):
        '''
        Entrées: un noeud et son rang dans le classement
        But : Fonction récursive pour parcourir l'arbre et remplir le classement provisoire 
        grace a leur niveau
        Sortie: None
        '''
        if noeud is None:
            return
        if noeud=='':
            return
        
        if noeud.feuille() and noeud.valeur is not None:
            # Ajouter les feuilles (joueurs initiaux) au classement
            classement_provisoire.append((noeud.valeur, niveau))
        else:
            # Parcours des sous-arbres
            parcours_provisoire(noeud.gauche, niveau + 1)
            parcours_provisoire(noeud.droit, niveau + 1)
            # Ajouter les gagnants intermédiaires au classement
            if noeud.valeur is not None:
                classement_provisoire.append((noeud.valeur, niveau))
                
    # Démarrer le parcours
    parcours_provisoire(arbre, 1)

    # Trier par niveau décroissant (vainqueur en premier), et éliminer les doublons
    classement_provisoire = sorted(classement_provisoire, key=lambda x: -x[1])
    # Ajouter des noeuds None quand il y a moins de 16 joueurs
    while len(classement_provisoire) < 16:
        classement_provisoire.insert(0, (None, 5))
    return [joueur[0] for joueur in classement_provisoire]


def reelclassement(classement_provisoire,duel2):
    """
    Entrée: le classement provisoire et la fonction duel2 pour départager les ex-aequo
    But: faire manuellement les arbres de duel d'ex-aequo
    Sortie: un tableau contenant le classement final du tournoi, après départage des ex-aequo
    """
    # Le tableau 'classement_provisoire' est a l'envers
    joueurs2=[] #=joueurs à la hauteur 2
    joueurs2.extend(classement_provisoire[12:14])
    joueurs3=[] #=joueurs à la hauteur 3 ...
    joueurs3.extend(classement_provisoire[8:12])
    joueurs4=[]
    joueurs4.extend(classement_provisoire[0:8])
        
    #constructions des arbres
    arbre2=construire_arbre(joueurs2)
    arbre3=construire_arbre(joueurs3)
    arbre4=construire_arbre(joueurs4)
    
    #lancement des duels
    arbre2.parcours2(duel2)
    arbre3.parcours2(duel2)
    arbre4.parcours2(duel2)
    
    #ajout des vrais gagnants dans le classement final
    classement_reel=[]
    #le premier et le second sont déjà connus
    classement_reel.append(classement_provisoire[15])
    classement_reel.append(classement_provisoire[14])
    
    #on ajoute le gagnant de l'arbre de duel du niveau 2 de l'arbre (3eme place)
    classement_reel.append(arbre2.valeur)
    #on ajoute le perdant du duel qui est donc 4eme
    if arbre2.gauche.valeur is not None:
        classement_reel.append(arbre2.gauche.valeur)
    elif arbre2.droit.valeur is not None:
        classement_reel.append(arbre2.droit.valeur)


    classement_reel.append(arbre3.valeur)
    if arbre3.gauche.valeur is not None:
        classement_reel.append(arbre3.gauche.valeur)
    elif arbre3.droit.valeur is not None:
        classement_reel.append(arbre3.droit.valeur)


    #on créer un nouvel arbre qui prend les perdants de l'arbre de niveau 3... ect
    joueurs5=[]

    if arbre3.gauche.gauche.valeur is not None:
        joueurs5.append(arbre3.gauche.gauche.valeur)
    else:
        joueurs5.append(arbre3.gauche.droit.valeur)
    if arbre3.droit.droit.valeur is not None:
        joueurs5.append(arbre3.droit.droit.valeur)
    else:
        joueurs5.append(arbre3.droit.gauche.valeur)
        
    arbre5=construire_arbre(joueurs5)   
    arbre5.parcours2(duel2)

    classement_reel.append(arbre5.valeur)
    if arbre5.gauche.valeur is not None:
        classement_reel.append(arbre5.gauche.valeur)
    elif arbre5.droit.valeur is not None:
        classement_reel.append(arbre5.droit.valeur) 
        
    classement_reel.append(arbre4.valeur)
    if arbre4.gauche.valeur is not None:
        classement_reel.append(arbre4.gauche.valeur)
    elif arbre4.droit.valeur is not None:
        classement_reel.append(arbre4.droit.valeur)
        


    joueurs6=[]

    if arbre4.gauche.gauche.valeur is not None:
        joueurs6.append(arbre4.gauche.gauche.valeur)
    else:
        joueurs6.append(arbre4.gauche.droit.valeur)
    if arbre4.droit.droit.valeur is not None:
        joueurs6.append(arbre4.droit.droit.valeur)
    else:
        joueurs6.append(arbre4.droit.gauche.valeur)
        
    arbre6=construire_arbre(joueurs6)   
    arbre6.parcours2(duel2)

    classement_reel.append(arbre6.valeur)
    if arbre6.gauche.valeur is not None:
        classement_reel.append(arbre6.gauche.valeur)
    elif arbre6.droit.valeur is not None:
        classement_reel.append(arbre6.droit.valeur)
        
        
    joueurs7=[]

    if arbre4.gauche.gauche.gauche.valeur is not None:
        joueurs7.append(arbre4.gauche.gauche.gauche.valeur)
    else:
        joueurs7.append(arbre4.gauche.gauche.droit.valeur)
    if arbre4.gauche.droit.droit.valeur is not None:
        joueurs7.append(arbre4.gauche.droit.droit.valeur)
    else:
        joueurs7.append(arbre4.gauche.droit.gauche.valeur)
    if arbre4.droit.gauche.gauche.valeur is not None:
        joueurs7.append(arbre4.droit.gauche.gauche.valeur)
    else:
        joueurs7.append(arbre4.droit.gauche.droit.valeur)
    if arbre4.droit.droit.droit.valeur is not None:
        joueurs7.append(arbre4.droit.droit.droit.valeur)
    else:
        joueurs7.append(arbre4.droit.droit.gauche.valeur)
         
    arbre7=construire_arbre(joueurs7)   
    arbre7.parcours2(duel2)
    
    classement_reel.append(arbre7.valeur)
    if arbre7.gauche.valeur is not None:
        classement_reel.append(arbre7.gauche.valeur)
    elif arbre7.droit.valeur is not None:
        classement_reel.append(arbre7.droit.valeur)


    joueurs8=[]

    if arbre7.gauche.gauche.valeur is not None:
        joueurs8.append(arbre7.gauche.gauche.valeur)
    else:
        joueurs8.append(arbre7.gauche.droit.valeur)
    if arbre7.droit.droit.valeur is not None:
        joueurs8.append(arbre7.droit.droit.valeur)
    else:
        joueurs8.append(arbre7.droit.gauche.valeur)
        
    arbre8=construire_arbre(joueurs8)   
    arbre8.parcours2(duel2) 

    classement_reel.append(arbre8.valeur)
    if arbre8.gauche.valeur is not None:
        classement_reel.append(arbre8.gauche.valeur)
    elif arbre8.droit.valeur is not None:
        classement_reel.append(arbre8.droit.valeur)
        
        
    print('\nClassement final :',classement_reel)
    return classement_reel




