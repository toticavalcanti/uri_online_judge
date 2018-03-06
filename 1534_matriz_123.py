# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 11:58:10 2018

@author: toti.cavalcanti
"""
while True:
    try:
        n = int(input())
        mat = [[0] * n] * n
        for i in range(n):
            for j in range(n):
                if  j == (n - 1) - i:
                    print(2, end = '')
                elif i == j:
                    print(1, end = '')
                else:                    
                    print(3, end = '')
            print()
#        for i in range(n):
#            print(''.join(str(e) for e in mat[i]))
                
    except(EOFError):
        break
