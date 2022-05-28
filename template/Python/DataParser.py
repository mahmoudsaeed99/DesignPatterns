# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:17:12 2022

@author: Mahmoud Saeed
"""

# from abc import ABC , abstractmethod

# class DataParser(ABC):
#     def parseDataAndGenerateOutput(self) -> None:
#         self.readData()
#         self.preocessData()
#         self.writeData()
    
#     @abstractmethod    
#     def readData(self) -> None:
#         pass
    
#     @abstractmethod
#     def precessData(self) -> None :
#         pass
    
    
#     def writeData():
#         print("writing")

from abc import ABC, abstractmethod


class DataParser(ABC):
    

    def parseDataAndGenerateOutput(self) -> None:

        self.readData()
        self.precessData()
        self.writeData()


    @abstractmethod
    def readData(self) -> None:
        pass

    @abstractmethod
    def precessData(self) -> None:
        pass
    
    def writeData(self):
        print("writing")
    