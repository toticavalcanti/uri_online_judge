# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:10:31 2018

@author: toti.cavalcanti
"""

lst = list(str(input()).split(" "))

for i in range(len(lst)):
    lst[i] = int(lst[i])
    
if lst[1] > lst[2] and lst[3] > lst[0] and lst[2] + lst[3] > lst[0] + lst[1] and lst[2] > 0 and lst[3] > 0 and lst[0] % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")