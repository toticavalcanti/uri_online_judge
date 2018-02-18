# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 13:06:08 2018

@author: toti.cavalcanti
"""

lines = int(input())

dic = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}

for i in range(lines):
    line = input()
    s = line.count('1') * dic['1'] + line.count('2') * dic['2'] + line.count('3') * dic['3'] + line.count('4') * dic['4'] + line.count('5') * dic['5'] + line.count('6') * dic['6'] + line.count('7') * dic['7'] + line.count('8') * dic['8'] + line.count('9') * dic['9'] + line.count('0') * dic['0']

    print("{} leds".format(s))