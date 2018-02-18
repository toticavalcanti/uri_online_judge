# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:42:37 2018

@author: toti.cavalcanti
"""
def Main():
  while True:
    hour1, min1, hour2 , min2 = map(int, input().split())
    if hour1 == min1 == hour2 == min2 == 0:
      break
    else:
      min1_final = hour1 * 60 + min1
      min2_final = hour2 * 60 + min2
      
      if(min2_final <= min1_final):
        min2_final += 24 * 60
      
      print(abs(min2_final - min1_final))
      
if __name__ == '__main__':
  Main()