#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:53:18 2023

@author: andrewwynn
"""

x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

xyz = [x, y, z]
print(xyz)


for i in xyz[:]:
    if i % 2 == 0:
        xyz.remove(i)

if len(xyz) == 0:
    print("None of the numbers are odd")

else:
    print("The largest odd number is ", max(xyz))