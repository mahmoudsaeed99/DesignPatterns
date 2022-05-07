# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:15:57 2022

@author: MahmoudSaeed
"""
import Vehicles


class Car(Vehicles.Vehicles):
    def accelerate(self):
        print("Car start to move")
    
    def pushBreak(self):
        print("Car Stop")
    
    def soundHorn(self):
        print("Beeeb")
        
        