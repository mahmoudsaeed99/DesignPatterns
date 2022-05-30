# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:23:25 2022

@author: Mahmoud Saeed
"""

from ISP import ISP

class Etisalat(ISP):
    browsingSpeed = 10
    
    def serverSite(self , url):
        return "http://{}.com".format(url)
        
    def setspeed(self , speed):
        self.browsingSpeed = speed
     
    def getspeed(self):
        return self.browsingSpeed
    
    