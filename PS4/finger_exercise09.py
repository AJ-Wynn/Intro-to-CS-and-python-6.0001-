#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 09:48:04 2023

@author: andrewwynn
"""

def findAnEven(L):
    for i in L:
        if i % 2 == 0:
            return i
    raise ValueError("The list 'L' does not contain an even number")
    

L = [1, 3, 5, 11, 9]
print(findAnEven(L))