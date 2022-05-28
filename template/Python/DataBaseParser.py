# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:40:43 2022

@author: Mahmoud Saeed
"""
from DataParser import DataParser

# class DataBaseParser(DataParser):
#     def readData():
#         print("data base read")
#     def precessData():
#         print("data base precess")


class DataBaseParser(DataParser):

    def readData(self) -> None:
        print("read db")

    def precessData(self) -> None:
        print("precess db")