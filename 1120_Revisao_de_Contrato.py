# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 19:49:18 2018

@author: toti.cavalcanti
"""

while True:
    try:
        d, n = (input().split())
        if d == '0' and  n == '0':
            break
        n = list(n)
        while d in n:
            n.remove(d)
        if n.count('0') == len(n):
            print(0)
        else:
            n = "".join(n)
            print(int(n))
            
    except(EOFError):
        break