# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:59:37 2018

@author: toti.cavalcanti
"""
import math

pi = 3.14159
gravity = 9.80665


def calcReach(alpha, velocity):
    alpha = alpha / 180.0  * pi 
    #horizontal component
    s_x = velocity * math.cos(alpha)
    #vertical component
    #sy = velocity * math.sin(alpha)
    z = gravity * height / (velocity * velocity)
    t = (velocity / gravity) * (math.sin(alpha) + math.sqrt(math.sin(alpha) * math.sin(alpha) + 2 * z))
    x = s_x * t
    return x

while True:
	try:
		height = float(input())
		loc_min, loc_max = input().split(" ")
		n = int(input())

		for i in range(n):
		    ang, vel = input().split(" ")
		    result = calcReach(float(ang), float(vel))
		    if result >= float(loc_min) and result <= float(loc_max):
		        print("{:.5f} -> DUCK".format(result))
		    else:
		        print("{:.5f} -> NUCK".format(result))
	except (EOFError):
		break