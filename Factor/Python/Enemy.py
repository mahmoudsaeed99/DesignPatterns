# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:04:32 2022

@author: MahmoudSaeed
"""
from abc import ABC

class Enemy():
    # def __init__(self , name , damage , health):
    #     self.name = name
    #     self.damage = damage
    #     self.health = health
        
        
    def setName(self , name):
        print(name,"_2")
        self.name = name
    
    def setDamage(self , damage):
        self.damage = damage
        
    def setHealth(self , health):
        self.health = health
    
    # def getHealth(self):
    #     return self.health
    
    # def getName(self):
    #     return self.name
    
    # def getDamage(self):
    #     return self.damage
    
    def showUp(self):
        print("name:  ",self.name);
        print("damage:  ",self.damage);
        print("health:  ",self.health);
        
        
        
    
    
        
        

