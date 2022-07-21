#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:09:00 2022

@author: aritdutta
"""

def gcd(x,y):
    f=[]
    if x<y:
        n=y
    if y<x:
        n=x
    for i in range(1,n+1):
        if x%i==0 and y%i==0:
            f.append(i)
    print(f[-1])