# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 11:21:15 2018

@author: toti.cavalcanti
"""

while True:
    n = int(input())
    
    if n == 0 :
        break
    t = 3
    mat = [[0] * n] * n
    result = []
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                mat[i][j] = 1
            else:
                mat[i][j] = min(n - i, min(i + 1, min(n - j, j + 1)))
        
        result.append(str(mat[i]))
    mat = []
    for string in result:
        mat.append(string.strip('[]'))
    
    for i in range(len(mat)):
        mat[i] = list(map(int, mat[i].split(", ")))
        
    for i in range(len(mat)):
        for j in range(len(mat)):
            num = "{0:>{width}}".format(str(mat[i][j]), width=t)
            if j == (len(mat) - 1):
                print(num)
            else:
                print(num, end = " ")	
    print()
