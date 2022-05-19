# -*- coding: utf-8 -*-
"""
Created on Thu May 19 16:57:44 2022

@author: Mahmoud Saeed
"""

import Item , ShoppingCart , PayPalStrategy , CreditCardStrategy

item1 = Item.Item("111",20)
item2 = Item.Item("222",40)
item3 = Item.Item("333",60)
item4 = Item.Item("444",80)
shop = ShoppingCart.ShoppingCart()
shop.addItem(item1)
shop.addItem(item2)
shop.addItem(item3)
shop.addItem(item4)
paypal = PayPalStrategy.PayPalStrategy
credit = CreditCardStrategy.CreditCardStrategy
shop.pay(credit)
shop.pay(paypal)
