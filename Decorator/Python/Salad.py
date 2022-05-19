# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:11:06 2022

@author: Mahmoud Saeed
"""

import SandwichDecorator

class Salad(SandwichDecorator.SandwichDecorator):
    
    def __init__(self , sandwich):
        super().__init__(sandwich)
        
    def getCost(self):
        return super().getCost() + 1.0 
    
    def getDesc(self):
        return super().getDesc() + " + Salad "