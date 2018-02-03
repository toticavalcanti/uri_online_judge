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
str = input()
lst = str.split(" ")

A = float(lst[0])
B = float(lst[1])
C = float(lst[2])

triangle_height = A * C / 2
circle_area = 3.14159 * C ** 2
trapezoid_area = (abs(A) + abs(B)) * abs(C) / 2
square_area = B ** 2
rectangle_area = A * B

print("TRIANGULO: {:.3f}".format(triangle_height))
print("CIRCULO: {:.3f}".format(circle_area))
print("TRAPEZIO: {:.3f}".format(trapezoid_area))
print("QUADRADO: {:.3f}".format(square_area))
print("RETANGULO: {:.3f}".format(rectangle_area))