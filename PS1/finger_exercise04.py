#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:41:23 2023

@author: andrewwynn
"""

import sys

x = int(input("Enter an integer: "))

if x == 0:
    print("Root and power undefined")
    sys.exit()
    
if x == 1:
    print("Root = 1")
    print("Power = 0")
    sys.exit()
    


for pwr in range(1, 6):
    root = 2
    while root**pwr < abs(x):
        root = root + 1
        
    
    if root**pwr != x:
        print("no pair of integers exist where root**pwr = x")
        continue
        
        
    else:
        print("Root = ", root)
        print("Power = ", pwr)
        break
        
        