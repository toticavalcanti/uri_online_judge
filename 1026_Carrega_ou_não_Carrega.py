# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:42:37 2018

@author: toti.cavalcanti
"""
while True:
    try:
        n1, n2 = input().split(" ")
        print("{}".format(int(n1) ^ int(n2)))
    
    except (EOFError):
        break