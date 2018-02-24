# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:50:32 2018

@author: toti.cavalcanti
"""
import re
#a = 97 até z = 122
n = int(input())


letters = []
for i in range(n):
    line = input()
    line = line.lower()
    line = re.sub('[^a-z]', '', line)
    dic = dict.fromkeys(line, 0)
    for c in line: dic[c] += 1
    
    maxValue = max(dic.values())
    result = [k for k, v in dic.items() if v == maxValue]
    print(''.join(sorted(result)))