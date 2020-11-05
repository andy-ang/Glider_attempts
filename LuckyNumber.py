# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:17:19 2020

@author: andya
"""

def solve(array,n):
    result = 0
    
    for i in array:
        current_number = i
        if i % 7 == 0:
            loop_cont = 1
            while (loop_cont == 1):
                if current_number % 7 == 0 and current_number != 1:
                    current_number = current_number / 7
                elif (current_number-1) % 7 == 0 and current_number != 1:
                    current_number = (current_number-1) / 7
                else:
                    loop_cont = 0
        if current_number == 1 and i != 1:
            result += 1
        
    return result


solve([1],4)