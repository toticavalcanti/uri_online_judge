# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:36:56 2018

@author: toti.cavalcanti
"""

#!/bin/python3

import sys

from math import sqrt

#T = int(input())

def isPrime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i is 0:
            return False
    return True

#
#for _ in range(T):
#    num = int(input())
#    print("Prime") if num >= 2 and isPrime(num) else print("Not Prime")

isPrime(31)