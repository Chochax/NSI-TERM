# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:17:02 2024


"""

"""
pile de carte avant distribution
"""
 
 
class Paquet:
    def __init__(self,paquet):
        self.paquet=paquet
        
    def distribuer(self,jeu1,jeu2):
        a = 2
        for elem in self.paquet:
            if a == 2:
                jeu1.append(elem) 
                a = 1  
            else:
                jeu2.append(elem)
                a = 2  

    
    
    
    
    
