# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:36:43 2018

@author: toti.cavalcanti
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:31:44 2018

@author: toti.cavalcanti
"""
nome = input()
salary = float(input())
sales_month = float(input())

commission = sales_month * 0.15

salary = salary + commission

print('TOTAL = R$ {:.2f}'.format(salary))