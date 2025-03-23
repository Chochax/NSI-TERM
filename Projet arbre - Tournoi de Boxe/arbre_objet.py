# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 08:05:19 2024

@author: MARION, EDWARD
"""
from random import *
from tkinter import *
class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur=valeur
        self.gauche=gauche
        self.droit=droit
            

    def feuille(self):
        '''
        Entrée : self(noeud)
        But : savoir si le noeud est une feuille
        Sortie : Booléen
        '''
        if self.gauche == '' and self.droit == '':
            return True
        else:
            return False
        
    def gagnant(self, enfant, fen, variable_pause, afficher_arbre,vainqueur, canvas, noeud, x, y, offset, bouton):
        '''
        Entrée : self(le parent) et l'enfant gagnant (+ les varibales d'affichage)
        But : faire monter de rang le gagnant du duel
        Sortie : None
        '''
        if enfant=='gauche':
            self.valeur=self.gauche.valeur
            message_gagnant=f"{self.gauche.valeur} a gagné le combat de boxe contre {self.droit.valeur}"
            self.gauche.valeur=None

        else:
            self.valeur=self.droit.valeur
            message_gagnant=f"{self.droit.valeur} a gagné le combat de boxe contre {self.gauche.valeur}"
            self.droit.valeur=None
        
        afficher_gagnant=Label(fen, text=message_gagnant, font=("Helvetica", 14), fg="green")
        afficher_gagnant.grid(row=3,column=0)
        # Mise en pause jusqu'à ce que la variable change
        afficher_arbre( canvas, vainqueur, x, y, offset)

        fen.wait_variable(variable_pause)
        variable_pause=0
        afficher_gagnant.destroy()
        if vainqueur.valeur is not None:
            variable_pause=1
            bouton.destroy()
            return
            

    def parcours(self, duel, fen, variable_pause, afficher_arbre,vainqueur, canvas, noeud, x, y, offset, bouton):
        """
        Entrée: une racine, la fonction duel du fichier 'main' (+ les varibales d'affichage)
        But :Parcourt un arbre binaire pour déterminer les actions à effectuer à chaque nœud.
        Cette méthode vérifie les valeurs des nœuds de l'arbre, effectue des duels entre nœuds
        ou détermine les gagnants en fonction de leurs états, et affiche les résultats
        dans l'interface graphique.
        Sortie : None
        """
        
        if self.valeur is None:
            if self.feuille():
                return
            self.gauche.parcours(duel, fen,variable_pause, afficher_arbre,vainqueur, canvas, noeud, x, y, offset, bouton)
            self.droit.parcours(duel,fen,variable_pause, afficher_arbre,vainqueur, canvas, noeud, x, y, offset, bouton)
        
        if self is None:
            return
        
        if self.feuille():
            return
        
        elif self.gauche.valeur is None and self.droit.valeur is not None:
            self.gagnant('droit',fen,variable_pause, afficher_arbre,vainqueur, canvas, noeud, x, y, offset, bouton)
            
        elif self.droit.valeur is None and self.gauche.valeur is not None:
            self.gagnant('gauche',fen,variable_pause, afficher_arbre,vainqueur, canvas, noeud, x, y, offset, bouton)
            
        elif self.gauche.valeur is not None and self.droit.valeur is not None:
            duel(self, fen, variable_pause, afficher_arbre,vainqueur, canvas, noeud, x, y, offset, bouton)
            return
        
        self.gauche.parcours(duel,fen,variable_pause, afficher_arbre,vainqueur, canvas, noeud, x, y, offset, bouton)
        self.droit.parcours(duel,fen, variable_pause, afficher_arbre,vainqueur, canvas, noeud, x, y, offset, bouton)
        variable_pause=1
        bouton=Button(fen, text='Fermer la fenêtre', command=lambda:fen.destroy())
        bouton.grid(row=2, column=0, sticky='e')
    
    
    
#------------METHODES COPIES POUR LE CLASSEMENT FINAL---------------------------------   
    
    
    def gagnant2(self, enfant):
        '''
        Entrée : self(le parent) et l'enfant gagnant
        But : faire monter de rang le gagnant du duel
        Sortie : None
        '''
        if enfant=='gauche':
            self.valeur=self.gauche.valeur
            print(self.gauche.valeur,'a gagné le combat de boxe contre', self.droit.valeur)
            self.gauche.valeur=None

        else:
            self.valeur=self.droit.valeur
            print(self.droit.valeur,'a gagné le combat de boxe contre', self.gauche.valeur)
            self.droit.valeur=None
    
    
    def parcours2(self,duel2):
        """
        Entrée: une racine, la fonction duel2 du fichier 'main'
        But : Parcourt un arbre binaire pour déterminer les actions à effectuer à chaque nœud.
        Cette méthode vérifie les valeurs des nœuds de l'arbre, effectue des duels entre nœuds
        ou détermine les gagnants en fonction de leurs états, et affiche les résultats
        dans l'interface graphique.
        Sortie : None
        """
                
        if self.valeur is None :
            if self.feuille() or self.gauche is None and self.droit is None:
                return
            self.gauche.parcours2(duel2)
            self.droit.parcours2(duel2)
        
        if self is None:
            return
        
        if self.gauche is None and self.droit is None:
            return
        
        elif self.gauche.valeur is None and self.droit.valeur is not None:
            self.gagnant2('droit')
            
        elif self.droit.valeur is None and self.gauche.valeur is not None:
            self.gagnant2('gauche')
            
        elif self.gauche.valeur is not None and self.droit.valeur is not None:
            duel2(self)
            return
        
        self.gauche.parcours2(duel2)
        self.droit.parcours2(duel2)
        
