#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 18:19:47 2023

@author: andrewwynn
"""

def isIn(x, y):
    if x in y:
        return True
    elif y in x:
        return True
    else:
        return False
    
print(isIn('yes', 'y'))