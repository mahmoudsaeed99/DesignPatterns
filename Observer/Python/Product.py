# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:55:16 2022

@author: MahmoudSaeed
"""

import Subject 

class Product(Subject.Subject):
    def __init__(self,name):
        self.name = name
        self.observerList = []
        self.availability = None
      
    def set_availability(self , available:bool):
        if available == True:
            self.availability = "availabel"
        else:
            self.availability = "not"
         
        self.notifyAllObserver()    
        
     
    def add(self , observer):
        self.observerList.append(observer)
        
    def remove(self , observer):
        if observer not in self.observerList:
            pass
        self.observerList.remove(observer)
        
    def notifyAllObserver(self):
        for i in self.observerList:
            i.update(self.availability)
            
            