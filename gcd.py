#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 11:18:05 2022

@author: aritdutta
"""

def gcd(x,y):
    X=[]
    Y=[]
    for i in range(1,(x+1)):
        if x%i==0:
            X.append(i)
    for i in range(1,(y+1)):
        if y%i==0:
            Y.append(i)
    Z=[]
    for i in X:
        if y%i==0:
            Z.append(i)
    print(Z[(len(Z))-1])
    
    
    
            