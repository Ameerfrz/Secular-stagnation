# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 15:43:11 2021

@author: Ameer
"""

import matplotlib.pyplot as plt
import numpy as np
import policy as pol
import production as pro
import Government as gov

β= .77
γ= .3
α = 0.7
Π_star = 1
i_star = 0
φ_π = 2 
D = 0.2  
g = 0.20
l_bar = 1
B_g= 0.02 
#change B_g to 0.02 if you wanna add fiscal policy
P_k= 0.40
δ = 0.79
A= 1.3
l_bar = 1
bvec = np.array([])

def saving(Π):
    '''
    --------------------------------------------------------------------
    Creates a vector for saving and borrowing of each generation
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: real interest rate
        
    OBJECTS CREATED WITHIN FUNCTION:
    b_y    = young generation borrowing
    b_m    = middle age generation saving
    bvec   = vector of saving or borrowing
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: bvec
    --------------------------------------------------------------------
    '''
    r=pol.real_interest(Π)
    b_y = D/(1+r)
    b_m = -(1+g) * b_y
    bvec=b_y, b_m
    return bvec


def consumption(Π):
    '''
    --------------------------------------------------------------------
    Creates a vector for consumption of each generation
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: real interest rate, wage
    labor, profit, saving , tax
        
    OBJECTS CREATED WITHIN FUNCTION:
    c_y    = young generation consumption
    c_m    = middle age generation consumption
    c_o    = old generation consumption
    cvec   = vector of consumption
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: cvec
    --------------------------------------------------------------------
    '''
    tvec = gov.tax(Π)
    bvec = saving(Π)
    r= pol.real_interest(Π)
    w= pro.wage(Π)
    L = pro.labor(Π)
    K= pro.capital(Π)
    z = pro.profit(Π)
    c_y = bvec[0] - tvec[0]
    c_m = w * L - (1+r) * bvec[0]+ z +  bvec[1] - tvec[1] - P_k * K
    c_o = - (1 + r) * bvec[1] - tvec[2] +  P_k * K * (1-δ)
    cvec= np.array([c_y,c_m,c_o])
    return cvec


def tc(Π):
    '''
    --------------------------------------------------------------------
    Summation of comsumption vector
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: consumption
        
    OBJECTS CREATED WITHIN FUNCTION:
    c    = total consumption
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: c
    --------------------------------------------------------------------
    '''
    cvec= consumption(Π)
    c= cvec.sum()
    return c


def Euler(Π,cvec):
    '''
    --------------------------------------------------------------------
    Calculates the Euler error for optimal loan supply
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    cvec = vector of consumption
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: real interest rate
        
    OBJECTS CREATED WITHIN FUNCTION:
    MU_cm    = middle age generation marginal utility of consumption
    MU_co    = old generation marginal utility of consumption
    error    = Euler error
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: error
    --------------------------------------------------------------------
    '''
    r= pol.real_interest(Π)
    MU_cm =  β / cvec[1] 
    MU_co = (β**2 * (1+r)) / cvec[2]
    error = MU_cm -  MU_co
    return error


def Euler_c(Π,cvec):
    '''
    --------------------------------------------------------------------
    Calculates the Euler error for optimal capital supply
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    cvec = vector of consumption
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: real rental rate on capital
        
    OBJECTS CREATED WITHIN FUNCTION:
    MU_cm    = middle age generation marginal utility of consumption
    MU_co    = old generation marginal utility of consumption
    error    = Euler error
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: error
    --------------------------------------------------------------------
    '''
    r_k= pro.rental(Π)
    MU_cm =  (P_k-r_k) / cvec[1] 
    MU_co = (P_k * (1-δ)) / cvec[2]
    error_c = MU_cm -  MU_co
    return error_c