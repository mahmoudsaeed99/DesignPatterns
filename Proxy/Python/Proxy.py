# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:32:08 2022

@author: Mahmoud Saeed
"""

from InternetProxy import InternetProxy

urls = ["facebook" , "youtube" , "twitter" , "instgram"]

internet = InternetProxy()
for i in urls:
    print(internet.serverSite(i))
    