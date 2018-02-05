# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:32:59 2018

@author: toti.cavalcanti
"""
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1016

dist = int(input())
res = abs(dist)/(90 - 60) * 60
print("{:.0f} minutos".format(res))