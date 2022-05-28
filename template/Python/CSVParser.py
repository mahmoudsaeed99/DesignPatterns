# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:42:08 2022

@author: Mahmoud Saeed
"""
from DataParser import DataParser

# class CSVParser(DataParser):
#     def readData():
#         print("csv read")
#     def precessData():
#         print("csv precess")

class CSVParser(DataParser):
 
    def readData(self) -> None:
        print("read CSV")

    def precessData(self) -> None:
        print("precess csv")