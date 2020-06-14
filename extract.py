#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:55:24 2020

@author: gavinwong
"""

import r2pipe
from os import listdir
import os

def iterate(foldername):
    for f in listdir(foldername):
            print(f)
    
##any command that runs in the r2 shell can be pased to the cmd method
def extract_write(filename):
    r = r2pipe.open(filename)
    s = r.cmd("pD 64")
    
    ##creating new text file
    slash = filename.rfind("/")
    txt_file = filename[slash + 1:] + ".txt"
    directory = "/Users/gavinwong/Desktop/Repos/SJUMalwareEnsembleResearch/"
    print(txt_file)
    
    f = open(os.path.join(directory, txt_file), "w+")
    f.write("DOS Header")
    f.write(s)
    f.close()
    return(str(directory + txt_file))


if __name__ == "__main__":
    s = extract_write("/Users/gavinwong/Desktop/Repos/SJUMalwareEnsembleResearch/VirusShare_fffb1996a5b7c4c716931af2842712e3")
    print(s)
    
    
    
            
