# -*- coding: utf-8 -*-
"""
Created on Wed May 18 22:15:05 2022

@author: Mahmoud Saeed
"""
import Command as command
import NoCommand as noCommand

class RemoteControl():
    onCommand = []
    offCommand = []
    
    def __init__(self):
        no_command = noCommand.NoCommand()
        for i in range(4):
            self.onCommand.append(no_command)
            self.offCommand.append(no_command)
            
        
    def addCommand(self , i , on_command , off_command):
              self.onCommand.insert(i ,on_command )  
              self.offCommand.insert(i ,off_command )
            
    def onButtonPressed(self , i):
         self.onCommand[i].excute()
     
    def offButtonPressed(self , i):
         self.onCommand[i].undo()
    

         