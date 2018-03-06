# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:26:33 2018

@author: toti.cavalcanti
"""


while True:
    try:
        n = int(input())
        line = list(map(int, input().split()))
        print(line.index(min(line)) + 1)
    except(EOFError):
        break
