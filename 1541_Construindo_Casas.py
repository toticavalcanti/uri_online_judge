# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:12:47 2018

@author: toti.cavalcanti
"""
import math
while True:
    
    line = list(map(int, input().split()))
    
    if len(line) == 1:
        break
    
    a = line[0]
    b = line[1]
    c = line[2]
    
    result = int(math.sqrt((a * b * 100) / c))
    print(result)