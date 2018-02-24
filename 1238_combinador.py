# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 17:16:57 2018

@author: toti.cavalcanti
"""

'''
2
Tpo oCder
aa bb

'''

n = int(input())

for i in range(n):
    lst = input().split(' ')
    string01 = lst[0]
    string02 = lst[1]
    result = []
    lenght_str_01 = len(string01)
    lenght_str_02 = len(string02)
    for i in range(min(lenght_str_01, lenght_str_02)):
        result.append(string01[i])
        result.append(string02[i])
    
    if lenght_str_01 < lenght_str_02:
        result.append(string02[lenght_str_01:])
    else:
        result.append(string01[lenght_str_02:])
    
    print( "".join(result))