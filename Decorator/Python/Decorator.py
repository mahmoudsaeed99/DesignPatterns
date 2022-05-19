# -*- coding: utf-8 -*-
"""
Created on Thu May 19 19:11:39 2022

@author: Mahmoud Saeed
"""

import BasicSandwich , Fool , Salad

# fool = Fool.Fool(BasicSandwich.BasicSandwich)

sandwich = Salad.Salad(Fool.Fool(BasicSandwich.BasicSandwich))

print(sandwich.getDesc())
print(sandwich.getCost())

