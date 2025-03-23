# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:43:09 2024

@author: EDWARD.COURJAUD, MARION THARREAU, ARTHUR GABORIAU
"""

import time
from tkinter import Button, PhotoImage, Label
from class_joueur import Joueur
from class_tower import Tower
from class_plateau import Case
from tkinter import Label

class Monstre:
    def __init__(self, pv, vitesse, niveau, revenu, label, photo):
        self.pv = pv
        self.vitesse = vitesse
        self.niveau = niveau
        self.revenu = revenu
        self.coordonnees = ()
        self.label = label
        self.photo = photo
        self.chemin = [(1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (4, 3), (4, 4), (4, 5), (3, 5), (2, 5), (1, 5), (1, 6), (1, 7)]
        self.etape = 0
        self.en_course = True  # Indique que le monstre est actif

    def avancer(self, joueur, fen):
        """
        Avance le monstre d'une case. Si le monstre atteint la dernière case,
        il est retiré de la grille et les PV du joueur sont réduits.
        """
        if self.en_course and self.etape < len(self.chemin) - 1:
            # Le monstre avance sur le chemin
            self.coordonnees = self.chemin[self.etape]
            self.etape += 1
            self.afficher_monstre()
        elif self.en_course:
            # Si le monstre atteint la fin du chemin, inflige ses PV restants au joueur
            print("Le monstre a atteint la fin du chemin.")
            joueur.perdre_pv(self.pv, fen)
            self.label.grid_remove()  # Retire le monstre de la grille Tkinter
            self.en_course = False   # Désactive le monstre pour éviter de redéclencher l'avancée
            
            
    def afficher_monstre(self):
        """
        Met à jour la position du monstre dans la grille Tkinter.
        """
        x, y = self.coordonnees
        self.label.config(image=self.photo)
        self.label.grid(row=x, column=y)

    def boucle_avancement(self, fen, joueur, intervalle=1000):
        """
        Boucle pour l'avancement du monstre.
        """
        if self.en_course:
            self.avancer(joueur, fen)
            # Relance la boucle si le monstre est encore en course
            if self.en_course:
                fen.after(intervalle, lambda: self.boucle_avancement(fen, joueur, intervalle))

    def perdre_pv(self, degats):
        self.pv -= degats
        if self.pv <= 0:
            print("Le monstre est éliminé !")
