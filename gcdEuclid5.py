#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 22:39:07 2022

@author: aritdutta
"""

def gcd(x,y):
    #Assume x=>y
    if x<y:
        (x,y)=(y,x)
    if x%y==0:
        return y
    else:
        r=x%y
    return gcd(y,r)