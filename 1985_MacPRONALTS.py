# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:44:31 2018

@author: toti.cavalcanti
"""
dic = {'1001': 1.50, '1002': 2.50,'1003': 3.50, '1004': 4.50, '1005': 5.50}

while True:
    try:
        p = int(input())  
        dic_qtd = {}
        for i in range(p):
            key, value = input().split()
            dic_qtd[key] = int(value)
        result = 0
        for key in dic_qtd:
            result += dic_qtd[key] * dic[key]
        print("{:.2f}".format(result))
    except(EOFError):
        break