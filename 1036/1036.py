# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:10:31 2018

@author: toti.cavalcanti
"""

lst = list(str(input()).split(" "))

for i in range(len(lst)):
    lst[i] = float(lst[i])
A = lst[0]
B = lst[1]
C = lst[2]

delta = (B ** 2) - (4 * A * C)

if delta < 0 or 2 * A == 0:
    print("Impossivel calcular") 

else :
    delta_root = delta ** 0.5
    x1 = ( -B + delta_root ) / ( 2 * A )
    x2 = ( -B - delta_root ) / ( 2 * A )
    
    print("R1 = {:.5f}".format(x1))
    print("R2 = {:.5f}".format(x2))