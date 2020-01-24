# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 13:24:33 2018

@author: toti.cavalcanti
"""
# A - Z
#65 - 90
# a - z
#97 - 122

num_lines = int(input())

#lines will be a list of character lists, 
#where each char list corresponds to a line of input in the input()
lines = []

for i in range(num_lines):
    lines.append([line for line in input()])



# first pass, shift 3 positions to the right in ASCII table.
for line in range(len(lines)):
    lines[line] = [chr(ord(char)+3) if (ord(char) in range(65, 91)) or (ord(char) in range(97, 123))
                     else char for char in lines[line]]

#second pass, reverses each line of the input lines
for line in lines:
    line.reverse()

#third pass, all characters from the middle onwards, 
#shift 1 character to the left in ASCII table
for i in range(len(lines)):
    for j in range(len(lines[i]) // 2, len(lines[i])):
        lines[i][j] = chr(ord(lines[i][j]) - 1)

#prints list elements as a string
for line in lines:
    print(''.join(str(char) for char in line))
    