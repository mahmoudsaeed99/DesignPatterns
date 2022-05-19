# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:02:10 2022

@author: Mahmoud Saeed
"""

import SandwichDecorator

class Fool(SandwichDecorator.SandwichDecorator):
    
    def __init__(self, sandwich):
         super().__init__(sandwich)
        
    def getCost(self):
        return super().getCost() + 2.0 
    
    def getDesc(self):
        return super().getDesc() + " + fool "