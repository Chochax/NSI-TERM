# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:20:09 2024

@author: EDWARD, MARION, ARTHUR
"""
from class_joueur import Joueur
from class_monstre import Monstre
from class_tower import Tower
from class_plateau import Case
from class_manche import Manche
from tkinter import *
from PIL import Image, ImageTk
from tkinter import *

# Création de la fenêtre principale
fen = Tk()
fen.title("Tower Defense")


def choisir_tour(x, y):
    """
    Entrée: Les coordonnées x(-> int) et y(-> int) de la case cliquée
    But: Renvoyer a la méthode 'placer_tour' pour choisir la tour a placer
    Sortie: Méthode placer_tour dans la classe plateau
    """
    boutons_case[(x, y)].proposition_tour(cadre_tour, tour1, tour2, tour3, images, joueur, fen, manque_argent, boutons_case, x, y)

def stopper_partie(*manches):
    for manche in manches:
        manche.arret_manche()
#----------------------------------------Création des cases
images = []
boutons_case = {}
t='terre'
c='chemin'        
map=[[t,t,t,t,t,t,t,t],
     [c,c,t,t,t,c,c,c],
     [t,c,t,t,t,c,t,t],
     [t,c,c,c,t,c,t,t],
     [t,t,t,c,c,c,t,t],
     [t,t,t,t,t,t,t,t]]
for x in range(6):
    for y in range(8):
        if map[x][y]=='terre':
            # Chargement de l'image
            photo = PhotoImage(file='image/carreau_herbe.png')
            images.append(photo)  # Ajout de l'image à la liste pour conserver la référence
    
            # Création du bouton avec l'image
            button = Button(fen, image=photo, bg='black', activebackground="red", command=lambda x=x, y=y: choisir_tour(x, y))
            button.grid(row=x, column=y)  # Placement du bouton dans la grille
            #button.bind("<Enter>", lambda e: button.config(bg="red")); button.bind("<Leave>", lambda e: button.config(bg="black"))

            case = Case(x, y, button, None)
            boutons_case[(x, y)] = case

        else:
            chemin = Label(fen,bg='black')
            chemin.grid(row=x, column=y, sticky="nsew")
            
# Création des tours
tour1=Tower(40, 1, 1, 1, 1,"image/tour_arc.png")
tour2=Tower(80, 2, 2, 2, 1,"image/tour_bombe.png")
tour3=Tower(120, 3, 3, 3, 1,"image/tour_feu.png")

joueur=Joueur(100, 200, Label(fen), Label(fen))

# Chargement des images de monstres
monstre1photo = PhotoImage(file='image/monstre1.png')
monstre2photo = PhotoImage(file='image/monstre2.png')
monstre3photo = PhotoImage(file='image/monstre3.png')
monstre4photo = PhotoImage(file='image/monstre4.png')
monstre5photo = PhotoImage(file='image/monstre5.png')

# Création des monstres
monstre1 = Monstre(3, 1, 1, 1, Label(fen), monstre1photo)
monstre1_copie = Monstre(3, 1, 1, 1, Label(fen), monstre1photo)
monstre1_copie2 = Monstre(3, 1, 1, 1, Label(fen), monstre1photo)
monstre1_copie3 = Monstre(3, 1, 1, 1, Label(fen), monstre1photo)
monstre1_copie4 = Monstre(3, 1, 1, 1, Label(fen), monstre1photo)
monstre1_copie5 = Monstre(3, 1, 1, 1, Label(fen), monstre1photo)
monstre1_copie6 = Monstre(3, 1, 1, 1, Label(fen), monstre1photo)


monstre2 = Monstre(5, 2, 2, 2, Label(fen), monstre2photo)
monstre2_copie = Monstre(5, 2, 2, 2, Label(fen), monstre2photo)
monstre2_copie2 = Monstre(5, 2, 2, 2, Label(fen), monstre2photo)
monstre2_copie3 = Monstre(5, 2, 2, 2, Label(fen), monstre2photo)
monstre2_copie4 = Monstre(5, 2, 2, 2, Label(fen), monstre2photo)
monstre2_copie5 = Monstre(5, 2, 2, 2, Label(fen), monstre2photo)
monstre2_copie6 = Monstre(5, 2, 2, 2, Label(fen), monstre2photo)
monstre2_copie7 = Monstre(5, 2, 2, 2, Label(fen), monstre2photo)
monstre2_copie8 = Monstre(5, 2, 2, 2, Label(fen), monstre2photo)
monstre2_copie9 = Monstre(5, 2, 2, 2, Label(fen), monstre2photo)
monstre2_copie10 = Monstre(5, 2, 2, 2, Label(fen), monstre2photo)

monstre3 = Monstre(8, 3, 3, 4, Label(fen), monstre3photo)
monstre3_copie = Monstre(8, 3, 3, 4, Label(fen), monstre3photo)
monstre3_copie2 = Monstre(8, 3, 3, 4, Label(fen), monstre3photo)
monstre3_copie3 = Monstre(8, 3, 3, 4, Label(fen), monstre3photo)
monstre3_copie4 = Monstre(8, 3, 3, 4, Label(fen), monstre3photo)
monstre3_copie5 = Monstre(8, 3, 3, 4, Label(fen), monstre3photo)
monstre3_copie6 = Monstre(8, 3, 3, 4, Label(fen), monstre3photo)
monstre3_copie7 = Monstre(8, 3, 3, 4, Label(fen), monstre3photo)
monstre3_copie8 = Monstre(8, 3, 3, 4, Label(fen), monstre3photo)

monstre4 = Monstre(10, 2, 4, 5, Label(fen), monstre4photo)
monstre4_copie = Monstre(10, 2, 4, 5, Label(fen), monstre4photo)
monstre4_copie2 = Monstre(10, 2, 4, 5, Label(fen), monstre4photo)
monstre4_copie3 = Monstre(10, 2, 4, 5, Label(fen), monstre4photo)
monstre4_copie4 = Monstre(10, 2, 4, 5, Label(fen), monstre4photo)
monstre4_copie5 = Monstre(10, 2, 4, 5, Label(fen), monstre4photo)

monstre5 = Monstre(15, 1, 5, 8, Label(fen), monstre5photo)
monstre5_copie = Monstre(15, 1, 5, 8, Label(fen), monstre5photo)
monstre5_copie2 = Monstre(15, 1, 5, 8, Label(fen), monstre5photo)
monstre5_copie3 = Monstre(15, 1, 5, 8, Label(fen), monstre5photo)


#Création boutons pour demarrer les manches
bouton_manche1 = Button(fen, text="Commencer manche 1", command=lambda: manche1.demarrer_manche1(manche1, manche2, joueur))
bouton_manche2 = Button(fen, text="Commencer manche 2", command=lambda: manche2.demarrer_manche2(manche2, manche3, joueur))
bouton_manche3 = Button(fen, text="Commencer manche 3", command=lambda: manche3.demarrer_manche3(manche3, manche4, joueur))
bouton_manche4 = Button(fen, text="Commencer manche 4", command=lambda: manche4.demarrer_manche4(manche4, manche5, joueur))
bouton_manche5 = Button(fen, text="Commencer manche 5", command=lambda: manche5.demarrer_manche5(manche5, joueur))

# Création de la manche avec les monstres créés
manche1 = Manche(fen, [monstre1, monstre1_copie, monstre1_copie2, monstre2], bouton_manche1)
manche2 = Manche(fen, [monstre1_copie3, monstre1_copie4, monstre2_copie, monstre2_copie2, monstre3], bouton_manche2)
manche3 = Manche(fen, [monstre2_copie3, monstre2_copie4, monstre2_copie5, monstre2_copie6, monstre3_copie, monstre3_copie2, monstre3_copie3, monstre4], bouton_manche3)
manche4 = Manche(fen, [monstre2_copie7, monstre2_copie8, monstre3_copie4, monstre3_copie5, monstre3_copie6, monstre4_copie, monstre4_copie2, monstre5], bouton_manche4)
manche5 = Manche(fen, [monstre1_copie5, monstre1_copie6, monstre2_copie9, monstre2_copie10, monstre3_copie7, monstre3_copie8, monstre4_copie3, monstre4_copie4, monstre4_copie5, monstre5_copie, monstre5_copie2, monstre5_copie3], bouton_manche5)

#------------------------------------Création des blocs d'informations---------------------------------#
cadre_info = LabelFrame(fen, text="Information joueur", padx=10, pady=10, bg="lightgrey", font=("Times New Roman", 20, "italic"))
cadre_info.grid(row=0, column=9, padx=20, pady=20, rowspan=2, sticky="new")  # Placement avec espacement autour

cadre_tour = LabelFrame(fen, text="Acheter une Tour", padx=10, pady=10, bg="lightgrey", font=("Times New Roman", 20, "italic"))
cadre_tour.grid(row=1, column=9, padx=20, pady=20, rowspan=5, sticky="sew")  # Placement avec espacement autour


info_argent=Label(cadre_info, text= f"Argent:{joueur.argent}", bg="lightgrey", font=("Trebuchet MS", 15))
info_argent.grid(row=0, column=0, sticky="w")

info_Pv=Label(cadre_info, text= f"PV:{joueur.pv}", bg="lightgrey", font=("Trebuchet MS", 15))
info_Pv.grid(row=1, column=0, sticky="w")

joueur=Joueur(10, 200, info_Pv, info_argent)#mise a jour du joueur

manque_argent=Label(fen, text="Vous n'avez pas assez d'argent pour\n acheter cette tour !", font=("Trebuchet MS", 10))
#manque_argent.grid(row=1, column=10)





# Ajouter un bouton pour arrêter la manche
bouton_arret= Button(fen, text="Arrêter la manche", command=lambda:manche1.arret_manche())
bouton_arret.grid(row=1, column=10)
bouton_manche1.grid(row=0, column=10)




fen.mainloop()
