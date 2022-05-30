# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:26:51 2022

@author: Mahmoud Saeed
"""
from ISP import ISP
from Etisalat import Etisalat

class InternetProxy(ISP):
    blockList = ['facebook' , 'twitter']
    
    def serverSite(self , url):
        self.logSite(url)
        if url in self.blockList:
            return "this site is blocked"
        else:
            return Etisalat().serverSite(url)
    
    
    def logSite(self , url):
        print("log into {}".format(url))