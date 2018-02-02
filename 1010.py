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
line1 = input() # lendo os números
line2 = input() # lendo os números
# quebrando a entrada em tokens separados por espaço 
line1 = line1.split(" ")
line2 = line2.split(" ")

val = int(line1[1]) * float(line1[2]) + int(line2[1]) * float(line2[2])

print("VALOR A PAGAR: R$ {:.2f}".format(val))