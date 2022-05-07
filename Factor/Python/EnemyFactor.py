# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:12:07 2022

@author: MahmoudSaeed
"""
from Turtle import  Turtle
from Bird import  Bird

class EnemyFactor():
    
    def createEnemy(id):
         if id == 1:
             print("Turtle")
             return Turtle()
             
         elif id == 2 :
             print("bird_1")
             return Bird()
         else:
             return None
         
            