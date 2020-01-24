# -*- coding: utf-8 -*-
"""

@author: toti.cavalcanti
"""
import time
from math import sqrt

T = int(input())

def isPrime_fast(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i is 0:
            return False
    return True


def isPrime(num):
    for i in range(2, num):
        if num % i is 0:
            return False
    return True



for n in range(T):
    num = int(input())
    t0= time.clock()
    print("Prime") if num >= 2 and isPrime_fast(num) else print("Not Prime")
    t1 = time.clock() - t0
    print("Time elapsed: ", t1 - t0)
