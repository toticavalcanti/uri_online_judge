# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:32:59 2018

@author: toti.cavalcanti
"""
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1021
num = float(input())
int_part = int(num)
fraction_part = num - int_part

bank_notes = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
coins = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

if num <= 0:
    print("NOTAS:") 
    for i in range(len(bank_notes)):
        print("{} nota(s) de R$ {:.2f}".format(0, float(bank_notes[i])))
    print("MOEDAS:") 
    for i in range(len(coins)):
        print("{} moeda(s) de R$ {:.2f}".format(0, float(coins[i])))

elif num == 1:
    print("NOTAS:") 
    for i in range(len(bank_notes)):
        print("{} nota(s) de R$ {:.2f}".format(0, float(bank_notes[i])))

    print("MOEDAS:") 
    qtd = int(int_part // coins[0])  
    print("{} moeda(s) de R$ {:.2f}".format(int(qtd), float(coins[0])))


else:
    print("NOTAS:")
    for bank_note in bank_notes:
        qtd = int(int_part // bank_note)  
        print("{} nota(s) de R$ {:.2f}".format(int(qtd), float(bank_note)))
        int_part = int(int_part % bank_note)
        
    print("MOEDAS:") 
    qtd = int(int_part // coins[0])  
    print("{}".format(qtd) + " moeda(s) de R$ " + str(coins[0]))
    for i in range(1, len(coins)):
        qtd = fraction_part // coins[i]
        print("{} moeda(s) de R$ {:.2f}".format(int(qtd), float(coins[i])))
        fraction_part = fraction_part % coins[i]
