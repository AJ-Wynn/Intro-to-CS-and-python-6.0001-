#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:49:08 2023

@author: andrewwynn
"""

s = '1.23,2.4,3.123'
s = s.split(',')
print(s)

sum = 0

for i in s:
    sum = sum + float(i)

print("Sum = ", sum)