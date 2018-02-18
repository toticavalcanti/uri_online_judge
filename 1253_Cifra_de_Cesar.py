# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:00:28 2018

@author: toti.cavalcanti
"""
# A - Z
#65 - 90

num_tests = int(input())

for i in range(num_tests):
    sentence = input()
    shift = int(input())
    res = []
    for char in sentence:
        if ord(char) - shift < 65:
            pos = 90 - (65 - (ord(char) - shift + 1))
            res.append(chr(pos))
        else:
            res.append(chr(ord(char) - shift))
    print("".join(res))
    