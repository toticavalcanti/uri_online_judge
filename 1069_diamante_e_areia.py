# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:45:06 2018

@author: toti.cavalcanti
"""

n = int(input())
for i in range(n):
    line = input()
    if line == '':
        continue
    op = 0 
    diamonds = 0
    for char in line:
        if char == '<':
            op += 1
        elif char == '>':
            if op > 0:
                op -= 1
                diamonds += 1
            
    print(str(diamonds))
    