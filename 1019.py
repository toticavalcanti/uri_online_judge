# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:32:59 2018

@author: toti.cavalcanti
"""
#https://www.urionlinejudge.com.br/judge/pt/problems/view/1019
total_segs = int(input())

hours = total_segs // 3600

segs_remaining = total_segs % 3600
minutes = segs_remaining // 60
segs_remaining_final = segs_remaining % 60


print("{}:{}:{}".format(hours, minutes, segs_remaining_final))