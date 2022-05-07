# -*- coding: utf-8 -*-
"""
Created on Sat May  7 17:38:08 2022

@author: MahmoudSaeed
"""

import Observer

class Managers(Observer.Observer):
    def __init__(self , name):
        self.name = name

    def update(self,message):
        print("Managers : {} got new notification:{}".format(self.name , message))