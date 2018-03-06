# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 17:28:13 2018

@author: toti.cavalcanti
"""

while(True):
    try:                 
        t1, t2, t3 , t4 = map(int, input().split())
        print(t1 + t2 + t3 + t4 - 3)
    except(EOFError):
        break