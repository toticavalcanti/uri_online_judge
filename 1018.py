# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:32:59 2018

@author: toti.cavalcanti
"""
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1017

num = int(input())

ballots = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00]

print("{}".format(num))
for ballot in ballots:
    qtd = int(num // ballot)  
    a = "{:,.2f}".format(ballot)
    b = a.replace(',','v')
    c = b.replace('.',',')
    print("{}".format(qtd) + " nota(s) de R$ " + c)
    num = int(num % ballot)