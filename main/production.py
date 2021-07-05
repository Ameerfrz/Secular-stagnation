# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 12:24:53 2021

@author: Ameer
"""

import matplotlib.pyplot as plt
import numpy as np
import policy as pol

β= .985
γ= .740
α = 0.7
Π_star = 1.01
φ_π = 2 
D = 0.28  
g = 0.25
l_bar = 1
B_g = 0
#change B_g to 0.1 if you wanna add fiscal policy


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
    if Π>=1:
        L_f=l_bar
        w= α * L_f**(α-1)
    else:
        w = ((1-γ) * α * (l_bar**(α-1)))/ (1-(γ * (Π **(-1))))
    return w


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
    w=wage(Π)
    if Π>=1:
        L=l_bar
    else:
        L = (w/α)**(1/(α-1))
    return L


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
    Y_s = L**α
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
    r_f= ((1+β)/β) * (((1+g) * D)/(1 - D))-1
    i_star = (1+r_f)*(Π_star)-1
    i=pol.interest(Π)
    if i>0:
        Y_d = D + ((1+β) * B_g )/(β) + ((1+β) * (1+g) * D * (1+i_star)**(-1) * (Π_star)**φ_π)/(β * (Π)**φ_π )
    else:
        Y_d = D + ((1+β) * B_g )/(β) + ((1+β) * (1+g) * D * (Π))/(β)
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
    z= Y_s-w*L
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



