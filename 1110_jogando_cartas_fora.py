# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 17:15:55 2018

@author: toti.cavalcanti
"""

while True:
    n = int(input())
    if n == 0 :
        break
    remaining = []
    for i in range(1,n+1):
        remaining.append(i)

    discarded = []
    while len(remaining) > 1:
        discarded.append(remaining.pop(0))
        remaining.insert(len(remaining) - 1,remaining.pop(0))

    print("Discarded cards: " + str(discarded).replace("[","").replace("]",""))
    print("Remaining card: " + str(remaining[0]))