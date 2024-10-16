# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:15:00 2024

@author: MARION.THARREAU, EDWARD COURJAUD
"""

class Joueur:
    def __init__(self,main=[], nom=''):
        self.main=main
        self.nom=nom
        
    
    def retourner_carte(self):
        return self.main.defiler()
    
    
    def gagner(self, carte1,carte2):
        tab_bataille=[]
        print(self.nom, 'a gagné')
        self.main.enfiler(carte1)
        self.main.enfiler(carte2)
        

