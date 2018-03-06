# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 18:00:32 2018

@author: toti.cavalcanti
"""
import math

while True:
    try:
        n = int(input())
        t = len(str(int(math.pow(2, (n - 1) * 2))))

        if n == 0:
            break
        mat = [[0 for x in range(n)] for y in range(n)]
        count = 0
        for i in range(n):
            power = count
            for j in range(len(mat)):
                mat[i][j] = 2 ** power
                power += 1
            count += 1
        
        for i in range(len(mat)):
            for j in range(len(mat)):
                num = "{0:>{width}}".format(str(mat[i][j]), width=t)
                if j == (len(mat) - 1):
                    print(num)
                else:
                    print(num, end = " ")	
        print()
    except(EOFError):
        break
