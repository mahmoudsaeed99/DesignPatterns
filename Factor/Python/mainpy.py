# -*- coding: utf-8 -*-
"""
Created on Sat May  7 18:13:53 2022

@author: MahmoudSaeed
"""
from EnemyFactor import EnemyFactor

for i in range(5):
    enemy = EnemyFactor.createEnemy(i%2 + 1 )
    enemy.showUp()
    