# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:23:13 2020

@author: Gavin
"""
list = []
import csv
with open("all_data.csv", "r") as readfile:
    reader = csv.reader(readfile)
    next(reader)
    previousRow = next(reader)
    list.append(previousRow)
    for row in reader:
        if row[1:] != previousRow[1:] and notCorrupted(row):
            list.append(row)
        previousRow = row
        
        
        
with open('all_data_new.csv', 'w', newline = '') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(list)
    

def notCorrupted(row):
    current = "-2"
    count = 0
    for cell in row[34:]:
        if current != cell:
            current = cell
            count = 0
        count += 1
        if count == 500:
            print(row)
            return False
    return True
        