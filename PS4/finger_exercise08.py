#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 17:09:25 2023

@author: andrewwynn
"""

def sumDigits(s):
    sum = 0
    
    for c in s:
        try:
            sum += int(c)
        except:
            continue
    return sum
            

s = 'a2b3c'
print(sumDigits(s))