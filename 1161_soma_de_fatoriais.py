# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:19:11 2018

@author: toti.cavalcanti
"""

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)
    
while True:
    try:
        n1, n2 = map(int, input().split())
        print(factorial(n1) + factorial(n2))
    except(EOFError):
        break