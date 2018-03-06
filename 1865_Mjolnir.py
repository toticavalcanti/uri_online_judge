# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 17:37:25 2018

@author: toti.cavalcanti
"""

c = int(input())

for i in range(c):
    name, power = input().split()
    if name == 'Thor':
        print('Y')
    else:
        print('N')