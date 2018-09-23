# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 23:53:32 2018

@author: D4C
"""

print("Hola")

def f(x):
    a = x ** 2
    b = a + g(a)
    return (a * b)

def g(x):
    a = x * 3
    return a ** 2

m = f(1)
n = g(1)
print (m, n)