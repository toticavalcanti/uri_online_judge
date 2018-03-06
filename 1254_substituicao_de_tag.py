# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 09:52:25 2018

@author: toti.cavalcanti
"""
def indexall(lst, value):
    return [i for i, v in enumerate(lst) if v == value]

while True:
    try:
        tag = input().lower()
        num = input()
        s = input().lower()
        l = []
        open_tag = False
        print(s)
        #<><BODY garbage>body</BODY>
        i = 0
        while i < len(s):
            if s[i] == '<' and open_tag == False:
                open_tag = True
                l.append(s[i])
                i += 1
            elif open_tag == False and s[i] == '>' or s[i] == '<' and open_tag == True:
                break
            elif s[i] == '>' and open_tag == True:
                l.append(s[i])
                i += 1
                open_tag = False
            elif open_tag == True:
                if s[i:i + len(tag)] == tag:
                    l.append(num)
                    i += len(tag)
                else:
                    l.append(s[i])
                    i += 1
        print("".join(l))        
                
                
        
        
    except(EOFError):
        break