#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 11:36:17 2018

@author: shahrzad
"""
import numpy as np
date_str='20181024'
directory='/home/shahrzad/Spyder/als/hpxmp-off-blas-indirect/data'
f=open(directory+'/bahram/10-24-18-0933/alsphx_20th_itrscs_1_40_700_20000_tree','r')
result=f.read()

als_tree=result.split('Tree information for function: als\n')[1].split('als;')[0]+'als;'
perf_data=result.split('Primitive Performance Counter Data in CSV:\n')[1].split('\n\nX:')[0].split('\n')
    
np.savetxt(directory+'/'+date_str+'_perfdata.csv', perf_data, delimiter=',', fmt='%s')

file=open(directory+'/'+date_str+'_als_tree.txt','w')
file.write(als_tree)
file.close()
