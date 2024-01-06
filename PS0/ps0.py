#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 19:10:40 2023

@author: andrewwynn
"""
import math

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
x_exp_y = x**y
logx = math.log(x, 2)

print("x**y = ", x_exp_y)
print("log(x) = ", int(logx))
