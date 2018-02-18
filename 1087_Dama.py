# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:42:37 2018

@author: toti.cavalcanti
"""
while True:
    x1, y1, x2, y2 = map(int, input().split())

    if (x1 + y1 + x2 + y2) == 0:
        break
    
    if (x1==x2) and (y1==y2):
        print("%d" %0)
        continue
    
    if (x1==x2) or (y1==y2):
        print("%d" %1)
        continue
    
    if abs(x1-x2) == abs(y1-y2):
        print("%d" %1)
        continue
    
    print("%d" %2)