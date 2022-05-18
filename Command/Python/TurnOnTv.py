# -*- coding: utf-8 -*-
"""
Created on Wed May 18 20:52:01 2022

@author: Mahmoud Saeed
"""

import Command as command

class TurnOnTv(command.Command):
    
    tv = None
    def __init__(self , tv):
        self.tv = tv
        
    def excute(self):
        self.tv.turnon()
    
    def undo(self):
        self.tv.turnoff()
    
    