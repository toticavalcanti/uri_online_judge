# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:28:33 2018

@author: toti.cavalcanti
"""

while True:
    try:
        t = int(input())
        line = list(map(int, input().split()))
        print(line.count(t))
        
        
    except(EOFError):
        break