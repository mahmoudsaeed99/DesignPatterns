# -*- coding: utf-8 -*-
"""
Created on Sat May 28 18:46:07 2022

@author: Mahmoud Saeed
"""

from CSVParser import CSVParser
from DataBaseParser import DataBaseParser


csv = CSVParser()
db = DataBaseParser()
csv.parseDataAndGenerateOutput()
