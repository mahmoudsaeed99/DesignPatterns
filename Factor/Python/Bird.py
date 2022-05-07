# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:09:54 2022

@author: MahmoudSaeed
"""
from Enemy import Enemy

class Bird(Enemy):
    # Enemy( "Bird" , 30 , 75)
    def __init__(self):
        Enemy.setName(Enemy , "bird")
        Enemy.setDamage(Enemy , 45)
        Enemy.setHealth(Enemy , 75)
    
    