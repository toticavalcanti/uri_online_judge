# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 16:54:46 2018

@author: toti.cavalcanti
"""

while(True):
    try:
        l = int(input())
        numbers = list(map(int, input().split()))
        maximum = max(numbers)
        if maximum < 10:
            print(1)
        elif maximum >= 10 and maximum < 20:
            print(2)
        else:
            print(3)
            
    except(EOFError):
            break