# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 17:57:50 2021

@author: Ameer
"""
import policy as pol
import numpy as np

β= .77
γ= .3
α = 0.7
Π_star = 1
i_star = 0
φ_π = 2 
D = 0.28  
g = 0.20
l_bar = 1
B_g= 0.02 
#change B_g to 0.1 if you wanna add fiscal policy
P_k= 0.35
δ = 0.79

T_y = 0
G = 0.03

def budget(Π):
    '''
    --------------------------------------------------------------------
    Given the relation between T_m and T_o, it calculates tax value using
    government bugdet constraint.
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None
        
    OBJECTS CREATED WITHIN FUNCTION:
    T     = tax value
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: T
    --------------------------------------------------------------------
    '''
    r= pol.real_interest(Π)
    T = (G + (((1+r)/(1+g))-1) * B_g)/(1+((β*(1+r))/(1+g)))
    return T


def tax(Π):
    '''
    --------------------------------------------------------------------
    Creates a vector for each generation tax value
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None
        
    OBJECTS CREATED WITHIN FUNCTION:
    T_m     = middle age household tax
    T_o     = old household tax
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: T
    --------------------------------------------------------------------
    '''
    T= budget(Π)
    r= pol.real_interest(Π)
    T_m = T
    T_o = (1+r) * β * T
    tvec= np.array([T_y,T_m,T_o])
    return tvec