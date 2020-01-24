# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:32:59 2018

@author: toti.cavalcanti
"""
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1021
value = eval(input()) 

hundred = fifty = twenty = ten = five = two = one = 0 
fiveCents = twentyFiveCents = tenCents = fiveCents = cents = 0 

value = float("%.2f" % value)
if int(value/100) >= 1:
 hundred = int(value/100) 
 value -= hundred*100 

value = float("%.2f" % value)
if int(value/50) >= 1:
  fifty = int(value/50) 
  value -=  fifty*50 

value = float("%.2f" % value)
if int(value/20) >= 1:
 twenty = int(value/20.00) 
 value -= twenty*20 

value = float("%.2f" % value)
if int(value/10) >= 1:
 ten = int(value/10) 
 value -= ten*10.00 

value = float("%.2f" % value)
if int(value/5) >= 1:
 five = int(value/5) 
 value -= five*5 

value = float("%.2f" % value)
if int(value/2) >= 1:
 two = int(value/2) 
 value -= two*2 

value = float("%.2f" % value)
if int(value/1) >= 1:
 one = int(value/1) 
 value -= one*1 

value = float("%.2f" % value)
if int(value/0.50) >= 1:
 fiveCents = int(value/0.50) 
 value -= fiveCents*0.50 

value = float("%.2f" % value)
if int(value/0.25) >= 1:
 twentyFiveCents = int(value/0.25) 
 value -= twentyFiveCents*0.25 

value = float("%.2f" % value)
if int(value/0.10) >= 1:
 tenCents = int(value/0.10) 
 value -= tenCents*0.10 

value = float("%.2f" % value)
if int(value/0.05) >= 1:
 fiveCents = int(value/0.05) 
 value -= fiveCents*0.05 

value = float("%.2f" % value)
if int(value/0.01) >= 0.998:
 cents = int(value/0.01) 
 value -= cents*0.01 

print("NOTAS:") 
print("%d nota(s) de R$ 100.00" % hundred) 
print("%d nota(s) de R$ 50.00" %  fifty) 
print("%d nota(s) de R$ 20.00" % twenty) 
print("%d nota(s) de R$ 10.00" % ten) 
print("%d nota(s) de R$ 5.00" % five) 
print("%d nota(s) de R$ 2.00" % two) 

print("MOEDAS:") 
print("%d moeda(s) de R$ 1.00" % one) 
print("%d moeda(s) de R$ 0.50" % fiveCents) 
print("%d moeda(s) de R$ 0.25" % twentyFiveCents) 
print("%d moeda(s) de R$ 0.10" % tenCents) 
print("%d moeda(s) de R$ 0.05" % fiveCents) 
print("%d moeda(s) de R$ 0.01" % cents) 