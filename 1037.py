# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:10:31 2018

@author: toti.cavalcanti
"""

num = float(input())

intervals = ["[0,25]", "(25,50]", "(50,75]", "(75,100]"]

if num < 0 or num > 100:
    print("Fora de intervalo")
elif num >= 0 and num <= 25:
    print("Intervalo {}".format(intervals[0]))
elif num > 25 and num <= 50:
    print("Intervalo {}".format(intervals[1]))
elif num > 50 and num <= 75:
    print("Intervalo {}".format(intervals[2]))
else:
    print("Intervalo {}".format(intervals[3]))