# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 11:50:24 2018

@author: toti.cavalcanti
"""
#Pedra-Papel-Tesoura-Lagarto-Spock
t = int(input())

for i in range(t):
    a, b = input().split()
    c = i + 1
    
    if(a == b):
        print("Caso #{}: De novo!".format(c))
    elif(a == "tesoura" and b == "papel"):
        print("Caso #{}: Bazinga!".format(c))
    elif(a == "papel" and b == "pedra"):
        print("Caso #{}: Bazinga!".format(c))
    elif(a == "pedra" and b == "lagarto"):
        print("Caso #{}: Bazinga!".format(c))
    elif(a == "lagarto" and b == "Spock"):
        print("Caso #{}: Bazinga!".format(c))
    elif(a == "Spock" and b == "tesoura"):
        print("Caso #{}: Bazinga!".format(c))
    elif(a == "tesoura" and b == "lagarto"):
        print("Caso #{}: Bazinga!".format(c))
    elif(a == "lagarto" and b == "papel"):
        print("Caso #{}: Bazinga!".format(c))
    elif(a == "papel" and b == "Spock"):
        print("Caso #{}: Bazinga!".format(c))
    elif(a == "Spock" and b == "pedra"):
        print("Caso #{}: Bazinga!".format(c))
    elif(a == "pedra" and b == "tesoura"):
        print("Caso #{}: Bazinga!".format(c))
    else:
        print("Caso #{}: Raj trapaceou!".format(c))