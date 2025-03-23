# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:45:45 2024

@author: EDWARD
"""
from tkinter import Button

class Manche:
    def __init__(self, fen, monstres, bouton_manche, intervalle_apparition=2000):
        """
        Initialise une manche.
        
        Args:
            fen: La fenêtre tkinter principale.
            monstres: Liste de monstres qui participeront à la manche.
            intervalle_apparition: Temps en millisecondes entre chaque apparition de monstre.
        """
        self.fen = fen
        self.monstres = monstres  # Liste des instances de Monstre pour cette manche
        self.intervalle_apparition = intervalle_apparition  # Délai entre apparitions
        self.monstres_actifs = []  # Liste pour stocker les monstres actifs en cours
        self.bouton_manche = bouton_manche

    def apparition_monstre(self, joueur):
        """ 
        Démarre l'apparition des monstres de la manche en les espaçant dans le temps.
        """
        # Apparaître chaque monstre avec un délai entre eux
        # Apparaître chaque monstre avec un délai entre eux
        for index, monstre in enumerate(self.monstres):
        # Planifie l'apparition de chaque monstre après un délai dépendant de l'indice du monstre
        # self.fen.after est utilisée pour déclencher l'apparition du monstre après index * self.intervalle_apparition millisecondes.
        # Le délai augmente progressivement pour chaque monstre en fonction de sa position (index) dans la liste.
            self.fen.after(index * self.intervalle_apparition, lambda m=monstre: self.deployer_monstre(m, joueur))
            # Utilisation de lambda m=monstre: 
            # Cette syntaxe permet de "capturer" la valeur actuelle de `monstre` dans `m` au moment de la boucle.
            # Sans cette capture, `monstre` référencerait toujours le dernier élément de la boucle en mémoire,
            # car `lambda` n'exécute `self.deployer_monstre(m)` qu'après le délai spécifié.
            # En verrouillant `monstre` dans `m`, chaque appel de `self.deployer_monstre(m)` reçoit le bon monstre.



    def deployer_monstre(self, monstre, joueur):
        """ Déploie un monstre en démarrant sa boucle d'avancement. """
        print(f"Déploiement du monstre de niveau {monstre.niveau}")
        self.monstres_actifs.append(monstre)
        monstre.boucle_avancement(self.fen, joueur, intervalle=1000)

    def debut_manche(self, joueur):
        """ Démarre l'apparition des monstres pour cette manche. """
        print("Début de la manche")
        self.apparition_monstre(joueur)
    
    def arret_manche(self):
        for monstre in self.monstres_actifs:
            monstre.label.grid_remove()  # Cache le monstre
        self.monstres_actifs.clear()# Vide la liste des monstres actifs pour préparer la prochaine manche
        print("fin manche")
    
    def demarrer_manche1(self, manche1, manche2, joueur):
        """ Commence la manche 1 et fait apparaitre le bouton pour commencer la manche 2 """
        # Démarrage de la manche
        manche1.debut_manche(joueur)
        manche2.bouton_manche.grid(row=0, column=10)
        
    def demarrer_manche2(self, manche2, manche3, joueur):
        """ Commence la manche 2 et fait apparaitre le bouton pour commencer la manche 3 """
        # Démarrage de la manche
        manche2.debut_manche(joueur)
        manche3.bouton_manche.grid(row=0, column=10)
        
        
    def demarrer_manche3(self, manche3, manche4, joueur):
        """ Commence la manche 3 et fait apparaitre le bouton pour commencer la manche 4 """
        # Démarrage de la manche
        manche3.debut_manche(joueur)
        manche4.bouton_manche.grid(row=0, column=10)
        
    def demarrer_manche4(self, manche4, manche5, joueur):
        """ Commence la manche 4 et fait apparaitre le bouton pour commencer la manche 5 """
        # Démarrage de la manche
        manche4.debut_manche(joueur)
        manche5.bouton_manche.grid(row=0, column=10)
        
    def demarrer_manche5(self, manche5, joueur):
        """ Commence la manche 5 """
        # Démarrage de la manche
        manche5.debut_manche(joueur)
