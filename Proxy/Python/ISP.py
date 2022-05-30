# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:09:22 2022

@author: Mahmoud Saeed
"""

from abc import ABC , abstractmethod

class ISP(ABC):
    
    @abstractmethod
    def serverSite(url):
        pass
    