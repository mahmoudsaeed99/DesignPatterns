# -*- coding: utf-8 -*-
"""
Created on Wed May 18 21:03:45 2022

@author: Mahmoud Saeed
"""

import Command as command

class TurnOffTv(command.Command):
    tv = None
    
    def __init__(self , tv):
        self.tv = tv 
        
    def excute(self):
        self.tv.turnoff()
    
    def undo(self):
        self.tv.turnon()
        