#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 22:26:09 2022

@author: aritdutta
"""

def gcd(x,y):
    #Assume x=>y
    if x<y:
        (x,y)=(y,x)
    while x%y!=0:
        diff=x-y
        (x,y)=(max(diff,y),min(diff,y))
    return y