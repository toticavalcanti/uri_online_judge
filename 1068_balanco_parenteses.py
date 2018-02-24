# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:39:01 2018

@author: toti.cavalcanti
"""

while True:
    try:
        open = True
        line = input()
        if line.count('(') != line.count(')'):
            print('incorrect')
        
        else:
            for char in line:
                if char == '(':
                    open = True
                else:
                    open = False
            if open: 
                print('incorrect')
            else:
                print('correct')    
        
    except(EOFError):
        break