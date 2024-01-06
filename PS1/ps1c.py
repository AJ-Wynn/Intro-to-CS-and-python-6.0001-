#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 11:56:22 2023

@author: andrewwynn
"""
import sys

portion_down_payment = 0.25
r = 0.04
semi_annual_raise = .07
total_cost = 1000000
total_months = 36
epsilon = 100
numGuesses = 0
current_savings = 0

annual_salary = float(input("Enter your starting annual salary: "))
annual_salary_copy = annual_salary

down_payment = total_cost * portion_down_payment

low = 0.00
high = 1.00
savings_rate = (high + low)/2.0

        
while abs(current_savings - down_payment) >= epsilon:
    print('low = ', low, 'high =', high, 'savings rate =', savings_rate )
    numGuesses += 1
    current_savings = 0
    months = 0
    annual_salary = annual_salary_copy
    
    savings_rate = (high + low)/2.0
    
    for i in range(total_months):
        current_savings += ((annual_salary / 12) * savings_rate) + (current_savings * r) / 12
        months += 1

        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
        
    print(current_savings)
    
    if current_savings < down_payment:
        low = savings_rate
    else:
        high = savings_rate
        
    if low == 1.0:
        print("It is not possible to pay the down payment in three years.")
        sys.exit()
    
    
    
    

print("Best savings rate: ", round(savings_rate, 4))
print("Steps in bisection search: ", numGuesses)


