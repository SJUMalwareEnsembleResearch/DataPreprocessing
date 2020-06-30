# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:23:13 2020

@author: Gavin
"""
import csv
import pandas as pd
list = []
with open("all_data2.csv", "r") as readfile:
    reader = csv.reader(readfile)
    next(reader)
    previousRow = next(reader)
    list.append(previousRow)
    for row in reader:
        if row[1:] != previousRow[1:] and notCorrupted(row) and moreThan1000(row):
            list.append(row)
        previousRow = row

dict = checkFilesPerFamily()

print(dict)
        
        
        
with open('all_data2_new.csv', 'w', newline = '') as writeFile:
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
        

def checkFilesPerFamily():
    dictionary = {'ADLOAD' : 0, 'AGENT' : 0, 'ALLAPLE_A' : 0, 'BHO' : 0, 'BIFROSE' : 0, 'CEEINJECT' : 0, 'CYCBOT_G' : 0, 'FAKEREAN' : 0,
                  'HOTBAR' : 0, 'INJECTOR' : 0, 'LOLYDA_BF' : 0, 'ONLINEGAMES' : 0, 'RENOS' : 0, 'RIMECUD_A' : 0, 'SMALL' : 0, 'STARTPAGE' : 0, 
                  'TOGA_RFN' : 0, 'VB' : 0, 'VBINJECT' : 0, 'VOBFUS' : 0 , 'VUNDO' : 0, 'WINTRIM_BX' : 0, 'WINWEBSEC' : 0, 'ZBOT' : 0, 'Family' : 0}
    with open('all_data2.csv', 'r') as readfile:
        reader = csv.reader(readfile)
        next(reader)
        for row in reader:
            dictionary[row[1]] += 1
    dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return dictionary

def moreThan1000(row):
    return "-1" not in row 

                
    
    