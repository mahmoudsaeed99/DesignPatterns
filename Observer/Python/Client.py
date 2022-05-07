# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:58:39 2022

@author: MahmoudSaeed
"""
import Observer

class Client(Observer.Observer):
    def __init__(self , name):
        self.name = name

    def update(self,message):
        print("Client : {} got new notification:{}".format(self.name , message))



