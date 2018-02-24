# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 23:19:27 2018

@author: toti.cavalcanti
"""
n = int(input())
for i in range(n):
    line =  input().split()
    x = int(line[0])
    y = int(line[1])
    rafael = (3 * x) * (3 * x) + y * y
    beto = 2 * (x * x) + (5 * y) * (5 * y)
    carlos = -100 * x + y * y * y
    
    if rafael > beto and rafael > carlos:
        print("Rafael ganhou")
    elif beto > rafael and beto > carlos:
        print("Beto ganhou")
    elif carlos > rafael and carlos > beto:
        print("Carlos ganhou")