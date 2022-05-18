# -*- coding: utf-8 -*-
"""
Created on Wed May 18 21:03:45 2022

@author: Mahmoud Saeed
"""

import Command as command

class TurnOffLight(command.Command):
    light = None
    
    def __init__(self , light):
        self.light = light 
        
    def excute(self):
        self.light.turnoff()
    
    def undo(self):
        self.light.turnon()
        