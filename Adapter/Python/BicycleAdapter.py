# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:18:19 2022

@author: MahmoudSaeed
"""

import Vehicles

class BicycleAdapter(Vehicles.Vehicles):
    def __init__(self , b):
        self.b = b
    def accelerate(self):
        self.b.pedal()
    
    def pushBreak(self):
        self.b.stop()
        
    def soundHorn(self):
        self.b.ringBell()