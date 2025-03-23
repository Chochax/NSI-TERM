# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:43:24 2024

@author: EDWARD.COURJAUD, MARION THARREAU, ARTHUR GABORIAU
"""
from tkinter import PhotoImage

class Tower:
    def __init__(self,prix,portee,degats,vitesse,niveau,image):
        self.prix=prix
        self.portee=portee
        self.degats=degats
        self.vitesse=vitesse
        self.niveau=niveau
        self.image=image
        
    def attaque(self):
        pass
    
    #def ameliorer(self):
        
    def placer(self,bouton,images,joueur, cadre_tour, fen, manque_argent, boutons_case, x, y):
        """
        Parameters
        ----------
        Entrée:
            bouton : Button (bouton cliqué)
            images : Liste ou les images des boutons du plateau sont enregistré
            joueur : objet Joueur
            info_argent : Label (indique l'argent du joueur)
            info_Pv : Label (indique le nombre de PV du joueur)
            cadre_tour : LabelFrame (cadre autour des propositions de tours)
            fen : Fenêtre tkinter du jeu
            manque_argent : Label (message d'erreur quand on a pas assez d'argent pour payer une tour)
        
        Rôle: Place une tour sur le plateau si le joueur a assez d'argent puis masque le cadre avec les propositions de tours
            
        Sortie: Une image tour sur la case cliqué, le cadre des tours disparait

        """
        if joueur.condition_placer_tower(self.prix, fen, manque_argent):
            photo = PhotoImage(file=self.image)
            images.append(photo)
            bouton.config(image=photo)
            cadre_tour.grid_forget()
            boutons_case[(x,y)].tour=self
    
    def vendre(self, bouton, images, joueur, boutons_case, x, y):
        joueur.argent+=boutons_case[(x,y)].tour.prix//2
        joueur.label_argent.config(text=f"Argent:{joueur.argent}")
        
        photo = PhotoImage(file='image/carreau_herbe.png')
        images.append(photo)       
        bouton.config(image=photo)