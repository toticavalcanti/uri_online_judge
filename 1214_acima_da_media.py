# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 09:35:17 2018

@author: toti.cavalcanti
"""

c = int(input())
for i in range(c):
    line = list(map(int, input().split()))
    number_of_students = line[0]
    class_notes = line[1:]
    
    class_average = sum(class_notes)/number_of_students
    
    #how many students above the class average
    number_students_above_average =  sum( student > class_average for student in class_notes )
    result = number_students_above_average / number_of_students
    print("{:.3f}%".format(result * 100))