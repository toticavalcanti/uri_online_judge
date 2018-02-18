# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:27:42 2018

@author: toti.cavalcanti
"""

while True:
    try:
        n = int(input())
        if n == 0:
            break
        results= list(map(int,input().split()))
        mary_won = results.count(0)
        john_won = results.count(1)
        
        print("Mary won {} times and John won {} times".format(mary_won, john_won))
    except (EOFError):
        break

