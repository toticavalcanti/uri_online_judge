# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:32:59 2018

@author: toti.cavalcanti
"""
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1019
total_days = int(input())

years = total_days // 365
months = total_days % 365 // 30
days = total_days % 365 % 30

print("{} ano(s)".format(years))
print("{} mes(es)".format(months))
print("{} dia(s)".format(days))