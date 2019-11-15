#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:15:56 2019

@author: abhishek
"""
f=open('/home/abhishek/Desktop/sketch_oct31a/a','r')
sachin=f.readlines()
f2=open('/home/abhishek/Desktop/sketch_oct31a/sachinodi.csv','r+')
sachinodi=f2.readlines()
#deciding column indexes
fields=sachin[0].split(',')
index_runs=fields.index('Runs')
index_year=fields.index('Start Date')
print(index_year)
print(index_runs)
def average(l,index_runs,index_year):
    year=[]
    del l[0]
    l1=[]
    y=[]
    rows=len(l)
    starting_year=0
    for i in range(0,25):   
        su=0
        n=0    
        for j in range(starting_year,rows):
            l1=l[j].split(',')
            y=l1[index_year].split(' ')
            year.append(y[2])
            t=year[0]
            if(year[n]!=t):
                break
            if(l1[index_runs]!='-'):
                su=su+int(l1[index_runs])
            else:
                su=su+0
           
            n=n+1
        starting_year=starting_year+n        
        l1.clear()
        year.clear()
        y.clear()
        if(n!=0):
            avg=su/n
        
        print('average in year,',t,' = ',avg)
def runsum(l,index_runs,index_year):
    year=[]
    del l[0]
    l1=[]
    y=[]
    rows=len(l)
    starting_year=0
    for i in range(0,25):   
        su=0
        n=0    
        for j in range(starting_year,rows):
            l1=l[j].split(',')
            y=l1[index_year].split(' ')
            year.append(y[2])
            t=year[0]
            if(year[n]!=t):
                break
            if(l1[index_runs]!='-'):
                su=su+int(l1[index_runs])
            else:
                su=su+0
           
            n=n+1
        starting_year=starting_year+n        
        l1.clear()
        year.clear()
        y.clear()       
        print('sum in year,',t,' = ',su)
        
#%%      
def yearhighest(l,index_runs,index_year):
    year=[]
    del l[0]
    l1=[]
    y=[]
    rows=len(l)
    starting_year=0
    run_L=[]
    for i in range(0,25):   
        run_L.clear()
        n=0    
        for j in range(starting_year,rows):
            l1=l[j].split(',')
            y=l1[index_year].split(' ')
            year.append(y[2])
            t=year[0]
            if(year[n]!=t):
                break
            if(l1[index_runs]!='-'):
               run_L.append(int(l1[index_runs])) 
            else:
               run_L.append(0) 
           
            n=n+1
        run_L.sort()
        Hrun=run_L[-1]
        H2run=run_L[-2]
        starting_year=starting_year+n        
        l1.clear()
        year.clear()
        y.clear()       
        print('higighest in year,',t,' = ',Hrun)
        print('second highest in year,',t,' = ',H2run)
yearhighest(sachin,index_runs,index_year)
























