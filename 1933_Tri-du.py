# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 11:42:20 2018

@author: toti.cavalcanti
"""

while (True):
    try:
        a, b = map(int, input().split())
        if a == b:
            print(a)
        elif a > b:
            print(a)
        else:
            print(b)
    except(EOFError):
        break