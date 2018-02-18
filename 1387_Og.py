# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:48:24 2018

@author: toti.cavalcanti
"""

while True:
    try:
        left, right = map(int,input().split())
        if left == 0 and right == 0:
            break
        print("{}".format(left + right))
    except (EOFError):
        break
    