#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 16:45:16 2023

@author: andrewwynn
"""

x = -8
epsilon = 0.01
numGuesses = 0
low = min(0.0, x)
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print('low = ', low, 'high = ', high, 'ans = ', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to the square root of', x)