# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 21:20:06 2018

@author: toti.cavalcanti
"""

n = int(input())

for i in range(n):
    days = 0
    qtd = float(input())
    while qtd > 1:
        qtd /= 2
        days += 1
    print('{} dias'.format(days))