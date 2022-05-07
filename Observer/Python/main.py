# -*- coding: utf-8 -*-
"""
Created on Sat May  7 17:07:24 2022

@author: MahmoudSaeed
"""

import Client
import Product 
import HRPerson
import Managers

product = Product.Product("mobile")
mahmoud = Client.Client("mahmoud")
mohamed = Client.Client("mohamed")
marwan = Client.Client("marwan")

ahmed = HRPerson.HRPerson("ahmed")
marwa = HRPerson.HRPerson("marwa")

saeed = Managers.Managers("saeed")
lamiaa = Managers.Managers("lamiaa")


product.add(mahmoud)
product.add(mohamed)
product.add(marwan)
product.add(ahmed)
product.add(marwa)
product.add(saeed)
product.add(lamiaa)


for i in range(5):
    available = i%2 == 0
    product.set_availability(available)
    if i == 2:
        product.remove(mahmoud)
    
    
