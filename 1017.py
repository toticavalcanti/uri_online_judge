# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:32:59 2018

@author: toti.cavalcanti
"""
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1017

time_spent_travel = int(input())
average_speed = int(input())
res = time_spent_travel * average_speed / 12
print("{:.3f}".format(res))