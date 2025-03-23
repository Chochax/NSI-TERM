# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:44:13 2024

@author: EDWARD, MARION, ARTHUR
"""
from tkinter import Label, Toplevel
import time

class Joueur:
    def __init__(self, pv, argent, label_pv, label_argent):
        self.pv = pv
        self.argent = argent
        self.label_pv = label_pv
        self.label_argent = label_argent
 
    def condition_placer_tower(self, prix_tower, fen, manque_argent):
        if self.assez_argent(prix_tower):
            self.argent -= prix_tower
            self.label_argent.config(text=f"Argent:{self.argent}")
            return True  # Tour peut être placée
        else:
            manque_argent.grid(row=1, column=9)
            fen.after(3000, manque_argent.grid_forget)
            print("Pas assez d'argent pour placer la tour")
            return False
 
    def assez_argent(self, prix_tower):
        return prix_tower <= self.argent

    def vendre(self, tower):
        self.argent+=tower.prix//2
        pass
 
    def perdre_pv(self, degats, fen):
        """Réduit les PV du joueur et met à jour l'affichage des PV."""
        self.pv -= degats
        if self.pv <= 0:
            print("Le joueur n'a plus de PV !")  # Ou une autre action pour la défaite
            #affiche une fenêtre par dessus le jeu pour dire que le joueur a perdu mais n'arrête pas le jeu
            self.pv=0
            self.label_pv.config(text=f"PV:{self.pv}")
            top = Toplevel(fen)
            label_popup = Label(top, bg="#ec6767", text="Vous avez perdu !", font=("Trebuchet MS", 60))
            label_popup.pack()
        # Mise à jour de l'affichage des PV dans le label
        else: 
            self.label_pv.config(text=f"PV: {self.pv}")
            print(f"Le joueur perd {degats} PV. PV restants: {self.pv}")
