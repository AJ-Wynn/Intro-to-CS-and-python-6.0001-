#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:26:01 2023

@author: andrewwynn
"""

counter = 0
int_list = []

while counter != 10:
    x = int(input("Enter 10 integers: "))
    int_list.append(x)
    counter += 1


for i in int_list[:]:
    if i % 2 == 0:
        int_list.remove(i)

if len(int_list) == 0:
    print("None of the numbers are odd")

else:
    print("The largest odd number is ", max(int_list))