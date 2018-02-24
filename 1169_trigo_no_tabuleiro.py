# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 00:21:26 2018

@author: toti.cavalcanti
"""

n = int(input())

for i in range(n):
    board_houses = int(input())
    double = [1]
    for i in range(1, board_houses):
        double.append(double[i - 1] * 2)

    total = sum(double)
    total_gram = total / 12
    total_kilo = total_gram / 1000
    
    print("{} kg".format(int(total_kilo)))