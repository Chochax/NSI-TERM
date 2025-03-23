# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:29:58 2024

@author: MARION
"""
from tkinter import Button, PhotoImage, Label
class Case:
    def __init__(self, row, column, bouton, tour):
        self.row=row
        self.column=column
        self.bouton=bouton
        self.tour=tour
        
    def proposition_tour(self, cadre_tour, tour1, tour2, tour3 ,images, joueur, fen, manque_argent, boutons_case, x, y):
        """
        Entrée:
            cadre_tour : LabelFrame (cadre autour des propositions de tours)
            tour1 : objet Tower
            tour2 : objet Tower
            tour3 : objet Tower
            images : Liste ou les images des boutons du plateau sont enregistré
            joueur : objet Joueur
            info_argent : Label (indique l'argent du joueur)
            info_Pv : Label (indique le nombre de PV du joueur)
            fen : Fenêtre tkinter du jeu
            manque_argent : Label (message d'erreur quand on a pas assez d'argent pour payer une tour) 
            
        Rôle: Permettre le choix d'une tour à placer'
            
        Sortie: Cadre(LabelFrame) avec les informations sur les tours (Button et Label)
        """
        cadre_tour.grid(row=1, column=9, padx=20, pady=20, rowspan=5, sticky="sew")
        #Définition des images
        tour_arc = PhotoImage(file='image/Tour_arc(base).png')
        images.append(tour_arc)
        tour_bombe = PhotoImage(file='image/Tour_bombe(base).png')
        images.append(tour_bombe)
        tour_feu = PhotoImage(file='image/Tour_feu(base).png')
        images.append(tour_feu)
        
        #Défintion des boutons et labels
        button_tour1 = Button(cadre_tour, bg='#2f4f99', image= tour_arc, command=lambda:tour1.placer(self.bouton, images, joueur, cadre_tour, fen, manque_argent, boutons_case, x, y))
        button_tour2 = Button(cadre_tour, bg="#2f4f99", image= tour_bombe, command=lambda:tour2.placer(self.bouton, images, joueur, cadre_tour, fen, manque_argent, boutons_case, x, y))
        button_tour3 = Button(cadre_tour, bg="#2f4f99", image= tour_feu, command=lambda:tour3.placer(self.bouton, images, joueur, cadre_tour, fen, manque_argent, boutons_case, x, y))
        
        prix_tour1=Label(cadre_tour, text="Prix=40\nPuissance=1", padx=10, bg="lightgrey", font=("Trebuchet MS", 10, "underline"))
        prix_tour2=Label(cadre_tour, text="Prix=80\nPuissance=2", padx=10, bg="lightgrey", font=("Trebuchet MS", 10, "underline"))
        prix_tour3=Label(cadre_tour, text="Prix=120\nPuissance=3", padx=10, bg="lightgrey", font=("Trebuchet MS", 10, "underline"))
        
        Acheter=Label(cadre_tour, text="Cliquez sur la tour pour l'acheter", background="lightgrey")
        vendre = Button(cadre_tour, bg="#ec6767", text="Vendre", font=(15), command=lambda:self.tour.vendre(self.bouton, images, joueur, boutons_case, x, y))
        
        #Placement des boutons et labels dans la grille        
        button_tour1.grid(column=0, row=1)
        button_tour2.grid(column=0, row=2)
        button_tour3.grid(column=0, row=3)
        
        prix_tour1.grid(column=1, row=1)
        prix_tour2.grid(column=1, row=2)
        prix_tour3.grid(column=1, row=3)
                
        Acheter.grid(column=0, row=0, columnspan=2, pady=10)
        vendre.grid(column=0, row=4, columnspan=2, pady=10)
