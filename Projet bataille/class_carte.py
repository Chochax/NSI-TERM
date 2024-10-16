# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:17:02 2024

@author: MARION.THARREAU, EDWARD COURJAUD
"""

class Carte:
    def __init__(self,couleur,nombre):
        self.couleur=couleur
        self.nombre=nombre
        
    def afficher_carte(self):
        return self.couleur,self.nombre
     
        