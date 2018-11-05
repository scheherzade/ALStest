#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:34:36 2018

@author: shahrzad
"""

import matplotlib.pyplot as plt
import numpy as np
import re
import glob
import os
import pandas as pd
import glob
from matplotlib.backends.backend_pdf import PdfPages


iteration_array=[1]
row_stop_array=[700]
num_factors_array=[40]
col_stop_array=[1000,10000,20000]
thr=[1, 2, 4, 8, 10, 12, 16]
   
d_phy={}
d_phy_gcc={}
d_py={}
d_phy_direct={}
for c in col_stop_array:
    d_phy[c]=[0]*len(thr)
    d_py[c]=[0]*len(thr)
    d_phy_gcc[c]=[0]*len(thr)
    d_phy_direct[c]=[0]*len(thr)


files = glob.glob('/home/shahrzad/src/phylanx_data/Python_vs_Phylanx/24OCT18/ALS_PYTHON/alspy_*')

for j in range(len(files)):
    filename=files[j]
    p=filename.split('/')[-1].replace("th","").split('_')
    th=int(p[1])
    i=int(p[3])
    fn=int(p[4])
    r=int(p[5])
    c=int(p[6])
    f=open(filename,'r').readlines()
    t=f[-1].split("= ")[-1].replace("\n","")
    d_py[c][thr.index(th)] = float(t)/float(i)
    


files = glob.glob('/home/shahrzad/src/phylanx_data/Python_vs_Phylanx/26OCT18/ALS_PHYLANX/alsphx_*')

for j in range(len(files)):
    filename=files[j]
    p=filename.split('/')[-1].replace("th","").split('_')
    th=int(p[1])
    i=int(p[3])
    fn=int(p[4])
    r=int(p[5])
    c=int(p[6])
    f=open(filename,'r').readlines()
    if len(f)!=0:
        for line in f:
            if 'time:' in line:
                t=line.split(" ")[1]
                d_phy[c][thr.index(th)]=(float(t)/float(i))     
                
                

files = glob.glob('/home/shahrzad/src/phylanx_data/Python_vs_Phylanx/ALS/31OCT18/ALS_PHYLANX/alsphx_*')

for j in range(len(files)):
    filename=files[j]
    p=filename.split('/')[-1].replace("th","").split('_')
    th=int(p[1])
    i=int(p[3])
    fn=int(p[4])
    r=int(p[5])
    c=int(p[6])
    f=open(filename,'r').readlines()
    if len(f)!=0:
        for line in f:
            if 'time:' in line:
                t=line.split(" ")[1]
                d_phy_gcc[c][thr.index(th)]=(float(t)/float(i))  
                
                
files = glob.glob('/home/shahrzad/src/phylanx_data/Python_vs_Phylanx/ALS/ALS_DIRECT/alsphx_*')

for j in range(len(files)):
    filename=files[j]
    p=filename.split('/')[-1].replace("th","").split('_')
    th=int(p[1])
    i=int(p[3])
    fn=int(p[4])
    r=int(p[5])
    c=int(p[6])
    f=open(filename,'r').readlines()
    if len(f)!=0:
        for line in f:
            if 'time:' in line:
                t=line.split(" ")[1]
                d_phy_direct[c][thr.index(th)]=(float(t)/float(i))  
         
#files = glob.glob('/home/shahrzad/Spyder/Rostam/hpxmp-off_blas_direct/2/alsphx_*_20000')
#results_phx_indirect_python = [0]*len(thr)
#
#for j in range(len(files)):
#    filename=files[j]
#    p=filename.split('/')[-1].replace("th","").split('_')
#    th=int(p[1])
#    i=int(p[3])
#    fn=int(p[4])
#    r=int(p[5])
#    c=int(p[6])
#    f=open(filename,'r').readlines()
#    t=f[-1].split("= ")[-1].replace("\n","")
#    results_phx_indirect_python[thr.index(th)] = float(t)/float(i)    
#    
pp = PdfPages('/home/shahrzad/Spyder/als/als_performance.pdf')
i=1
for c in col_stop_array:
    plt.figure(i)
    #plt.plot(thr,results_phx_direct,label='phx_direct',marker='o')
    plt.plot(thr,d_phy[c],label='phx_physl',marker='+')
    plt.plot(thr,d_py[c],label='python',marker='x')
    plt.plot(thr,d_phy_gcc[c],label='phx_physl_avx2',marker='+')
    plt.plot(thr,d_phy_gcc[c],label='phx_physl_cpp',marker='+')


    plt.title("700-40-"+str(c))
    plt.xlabel("#threads")
    plt.ylabel("Execution time(seconds)")
    plt.legend()
    i=i+1

    plt.savefig(pp, format='pdf',bbox_inches='tight')
    print('')
plt.show()
pp.close()    
