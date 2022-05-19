# -*- coding: utf-8 -*-
"""
Created on Thu May 19 16:51:59 2022

@author: Mahmoud Saeed
"""


class ShoppingCart():
    items = []
    
    def addItem(self , item):
        self.items.append(item)
    
    def pay(self , payment):
        if len(self.items) == 0:
            print("No items in cart")
        else:
            payment.pay()
            print("clear cart ...... ")
            del(self.items[:])
            print("cleared ")
        
        
            
        