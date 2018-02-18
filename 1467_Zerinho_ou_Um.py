# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 46:17:42 2018

@author: toti.cavalcanti
"""

while True:
    try:
        players = ['A', 'B', 'C']
        results= list(map(int,input().split()))
        if results.count(0) == 3 or results.count(1) == 3:
            print('*')
        elif results.count(0) < results.count(1):
            print(players[results.index(0)])
        else:
            print(players[results.index(1)])
    
    except (EOFError):
        break

