# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:52:01 2022

@author: Mahmoud Saeed
"""

import Command as command

class TurnOnLight(command.Command):
    
    light = None
    def __init__(self , light):
        self.light = light
        
    def excute(self):
        self.light.turnon()
    
    def undo(self):
        self.light.turnoff()
    
    