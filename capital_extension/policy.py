# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:19:04 2021

@author: Ameer
"""
import matplotlib.pyplot as plt
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
P_k= 0.45
δ = 0.79

def interest(Π):
    '''
    --------------------------------------------------------------------
    Takes a given inflation value, and calculates the correspanding 
    interest rate based on Taylor rule and zero lower bound.
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None
        
    OBJECTS CREATED WITHIN FUNCTION:
    r_f     = full-employment real interest rate
    i_star = target inflation
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: i
    --------------------------------------------------------------------
    '''
    i_p= (1+i_star) * (((Π/Π_star)**φ_π))-1
    if i_p>0:
        i=i_p
    else:
        i=0
    return i


def real_interest(Π):
    '''
    --------------------------------------------------------------------
    Calculates the real interest rate using fisher equation.
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: inflation
        
    OBJECTS CREATED WITHIN FUNCTION:
    r     = real interest rate
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: r
    --------------------------------------------------------------------
    '''
    i = interest(Π)
    r = ((1+i)/Π)-1
    return r


r_map = np.vectorize(real_interest)
Π = np.arange(0.80, 1.20, 0.005)
r= r_map(Π)
plt.plot(Π, r)
plt.show() 

  
