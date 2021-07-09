# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:24:53 2021

@author: Ameer
"""

import matplotlib.pyplot as plt
import numpy as np
import policy as pol

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
P_k= 0.3
δ = 0.79
A= 1.25

def rental(Π):
    r = pol.real_interest(Π)
    r_k =  P_k * (1-((1-δ)/(1+r)))
    return r_k


def labor(Π):
    '''
    --------------------------------------------------------------------
    Calculates the correspanding lebor level for each environment.
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: wage
        
    OBJECTS CREATED WITHIN FUNCTION:
    L    = endogenous Labor
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: L
    --------------------------------------------------------------------
    '''
    if Π>=1:
        L=l_bar
    else:
        L = ((1-(γ/Π))/(1-γ))**(1/(1-α)) * l_bar
    return L


def capital(Π):
    r_k = rental(Π)
    L= labor(Π)
    if Π>=1:
        K= (((1-α)*A)/r_k) ** (1/α)
    else:
        K = (((1-α)*L*A)/r_k) ** (1/α)
    return K


def wage(Π):
    '''
    --------------------------------------------------------------------
    The wage equation differs based on inflation. The function defines the 
    wage for two environments based on inflation.
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None
        
    OBJECTS CREATED WITHIN FUNCTION:
    L_f    = Full-employment level - predifined in the model
    w      = real wage 
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: w
    --------------------------------------------------------------------
    '''
    K= capital(Π)
    if Π>=1:
        w= α * A * K**(1-α)
    else:
        w = ((1-γ) * α * A * (K**(1-α)))/ (1-(γ * (Π **(-1))))
    return w




def aggregates_s(Π):
    '''
    --------------------------------------------------------------------
    Takes the labor supply and calculates the aggregate supply.
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: labor
        
    OBJECTS CREATED WITHIN FUNCTION:
    L    = endogenous Labor
    Y_s  = aggregate supply
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: Y_s
    --------------------------------------------------------------------
    '''
    L= labor(Π)
    K= capital(Π)
    Y_s = A * (L**α) * (K**(1-α))
    return Y_s


"""
Note: The aggregates_s function is not continous, which poses restrictations 
on how to solve for SS. For intance, bisection method would not work.
"""


def aggregates_d(Π):
    '''
    --------------------------------------------------------------------
    calculates the aggregate demand.
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: interest
        
    OBJECTS CREATED WITHIN FUNCTION:
    r_f     = full-employment real interest rate
    i_star = target inflation
    i    = interest rate 
    Y_d  = aggregate demand
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: Y_d
    --------------------------------------------------------------------
    '''

    i=pol.interest(Π)
    K= capital(Π)
    r= pol.real_interest(Π)
    if i>0:
        Y_d = D + ((1+β) * (1+g) * D )/(β*(1+r)) + ((1+β) * B_g )/(β)+  P_k * K * (1+ ((1/(β*(1+r)))*(1-δ)))
    else:
        Y_d = D + ((1+β) * (1+g) * D )/(β*(1+r)) + ((1+β) * B_g )/(β) + P_k * K * (1+ ((Π/β)*(1-δ)))
    return Y_d


def profit(Π):
    '''
    --------------------------------------------------------------------
    calculates the firm profit that goes to middle-age household
    --------------------------------------------------------------------
    INPUTS:
    Π    = Inflation
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: aggregates_s, wage, labor
        
    OBJECTS CREATED WITHIN FUNCTION:
    z    = firms profit
    
    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: z
    --------------------------------------------------------------------
    '''
    Y_s=aggregates_s(Π)
    w= wage(Π)
    L = labor(Π)
    K= capital(Π)
    r_k= rental(Π)
    z= Y_s-w*L-P_k* r_k * K
    return z


error_m = np.vectorize(aggregates_s)
Π = np.arange(0.80, 1.20, 0.005)
r= error_m(Π)
plt.plot(r, Π)
plt.show() 

error_m = np.vectorize(aggregates_d)
Π = np.arange(0.80, 1.20, 0.005)
r= error_m(Π)
plt.plot(r, Π)
plt.show() 


