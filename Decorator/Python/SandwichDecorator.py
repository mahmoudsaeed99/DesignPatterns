# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:58:11 2022

@author: Mahmoud Saeed
"""

from abc import ABCMeta
import six


import Sandwich

@six.add_metaclass(ABCMeta)
class SandwichDecorator(Sandwich.Sandwich):
    
    sandwich = None
    
    def __init__(self , sandwich):
        self.sandwich = sandwich
        
    def getDesc(self):
        return self.sandwich.getDesc()
    
    def getCost(self):
        return self.sandwich.getCost()
    
    
    