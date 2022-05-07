# -*- coding: utf-8 -*-
"""
Created on Sat May  7 17:35:44 2022

@author: MahmoudSaeed
"""

import Observer

class HRPerson(Observer.Observer):
    def __init__(self , name):
        self.name = name

    def update(self,message):
        print("HR : {} got new notification:{}".format(self.name , message))