# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:18:43 2022

@author: MahmoudSaeed
"""

import Car , Bicycle , BicycleAdapter , Vehicles

car = Car.Car();
car.accelerate()
car.pushBreak()
car.soundHorn()
bicycle = BicycleAdapter.BicycleAdapter(Bicycle.Bicycle())
bicycle.accelerate()
bicycle.pushBreak()
bicycle.soundHorn()

