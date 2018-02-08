# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:10:31 2018

@author: toti.cavalcanti
"""

lst = list(str(input()).split(" "))

dic = {'1': 4.00, '2': 4.50, '3': 5.00, '4': 2.00, '5': 1.50}

print("Total: R$ {:.2f}".format(dic[lst[0]] * int(lst[1])))