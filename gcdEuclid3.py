#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 22:09:17 2022

@author: aritdutta
"""

def gcd(x,y):
    #Assume x=>y
    if x<y:
        (x,y)=(y,x)
    if x%y==0:
        return y
    else:
        diff=(x-y)
        return gcd(max(diff,y),min(diff,y))