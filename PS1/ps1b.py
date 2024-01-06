#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:50:14 2023

@author: andrewwynn
"""

portion_down_payment = 0.25
current_savings = 0.00
r = 0.04

annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

down_payment = total_cost * portion_down_payment

months = 0

while True:
    current_savings += ((annual_salary / 12) * portion_saved) + (current_savings * r) / 12
    months += 1
    
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        
    
    if current_savings >= down_payment:
        print("Number of months: ", months)
        break
    