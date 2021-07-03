# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:19:04 2021

@author: Ameer
"""
import matplotlib.pyplot as plt
import numpy as np

β= .985
γ= .790
α = 0.7
Π_star = 1.01
φ_π = 2 
D = 0.28  
g = 0.25
l_bar = 1


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
    r_f= ((1+β)/β) * (((1+g) * D)/(1 - D))-1
    i_star = (1+r_f)*(Π_star)-1
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

