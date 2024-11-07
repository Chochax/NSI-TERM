# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:14:53 2024


"""

class Main:
    def __init__(self, carte):
        self.carte=carte
        
        
    def enfiler(self, carte):
        self.carte=[carte]+self.carte   
        
    def defiler(self):
        # Retire la première carte de la main (si la main n'est pas vide)
        if self.carte:
            return self.carte.pop(0)
        else:
            return self.est_vide  # Si la main est vide : perdu
    
    def est_vide(self):
        if len(self.valeurs)==0:
            return True
        else:
            return False
           
        
