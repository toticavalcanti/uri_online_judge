# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:59:00 2018

@author: toti.cavalcanti
"""

while True:
    try:
        n = int(input())
        lst = []
        for i in range(n):
            lst.append(input())
        print('Ciencia da Computacao')
    except(EOFError):
        break