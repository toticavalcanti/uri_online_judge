# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 17:16:21 2018

@author: toti.cavalcanti
"""

n = int(input())

for i in range(n):
    m = int(input())
    lst = []
    dic_buy = {}
    dic_market = {}
    for j in range(m):
        lst = input().split()
        #treat compound words
        if len(lst) > 2:
            lst[0] = " ".join(lst[:-1])
            del lst[1:-1]
        dic_market[lst[0]] = lst[1]
    
    p = int(input(  ))
    lst = []
    for j in range(p):
        lst = input().split()
        #treat compound words
        if len(lst) > 2:
            lst[0] = " ".join(lst[:-1])
            del lst[1:-1]
        dic_buy[lst[0]] = lst[1]
      
    result = 0
    for key in dic_buy:
        result += float(dic_buy[key]) * float(dic_market[key])
    
    print("R$ {:.2f}".format(result))

    