# -*- coding: utf-8 -*-
"""
Fri Jul  2 20:19:04 2021

@author: Ameer
"""

import matplotlib.pyplot as plt
import numpy as np
import policy as pol
import production as pro
import household as house


β= .985
γ= .790
α = 0.7
Π_star = 1.01
φ_π = 2 
D = 0.28  
g = 0.25
l_bar = 1


def excess(Π):
    Y_s = pro.aggregates_s(Π)
    Y_d = pro.aggregates_d(Π)
    excess = Y_s - Y_d
    return excess

def brute():
    '''
    --------------------------------------------------------------------
    Exhaustive Enumeration method to determine the intersection point of
    aggregate supply and demand
    --------------------------------------------------------------------
    INPUTS:
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: excess
        
    OBJECTS CREATED WITHIN FUNCTION:
    roots    = vector of intersection points
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: error
    --------------------------------------------------------------------
    '''
    roots = []
    increment = 0.00025
    i=0.8
    while i<=1.4:
        if excess(i) * excess(i+increment)  < 0:
            root = i
            roots.append(root)
            i+= increment
        else:
            i+= increment
    return roots
print(brute())

error_m = np.vectorize(excess)
Π = np.arange(0.80, 1.20, 0.005)
r= error_m(Π)
plt.plot(r, Π)
plt.show() 
