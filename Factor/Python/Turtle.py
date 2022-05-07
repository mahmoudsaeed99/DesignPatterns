# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:11:28 2022

@author: MahmoudSaeed
"""
from Enemy import Enemy

class Turtle(Enemy):
    def __init__(self):
        Enemy.setName(Enemy , "Turtle")
        Enemy.setDamage(Enemy , 40)
        Enemy.setHealth(Enemy , 55)
    
    