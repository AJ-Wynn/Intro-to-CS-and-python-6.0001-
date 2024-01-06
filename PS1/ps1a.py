#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 11:55:01 2023

@author: andrewwynn
"""

portion_down_payment = 0.25
current_savings = 0.00
r = 0.04

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

down_payment = total_cost * portion_down_payment

months = 0

while True:
    current_savings += ((annual_salary / 12) * portion_saved) + (current_savings * r) / 12
    months += 1

    
    if current_savings >= down_payment:
        print("Number of months: ", months)
        break
    
                      
                    