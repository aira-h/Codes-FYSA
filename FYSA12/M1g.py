# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 09:27:16 2024

@author: Aira
"""

import numpy as np 
import matplotlib.pyplot as plt 
import numpy.linalg as la
from matplotlib.patches import *


t_10=[5.43,5.56,5.43,5.50,5.50]
t_10_avg=sum(t_10)/len(t_10)
T_10=t_10_avg/5
t_20=[5.34,5.31,5.56,5.62,5.43]
t_20_avg=sum(t_20)/len(t_20)
T_20=t_20_avg/5
t_10_again=[11.18,11.31,11.25,11.5,11.31]
t_10_again_avg=sum(t_10_again)/len(t_10_again)
T_10_again=t_10_again_avg/10
t_20_again=[11.31,11.31,11.31,11.31,11.37]
t_20_again_avg=sum(t_20_again)/len(t_20_again)
T_20_again=t_20_again_avg/10
reaction=1.25
stopwatch_error=.005
error_for_a=np.sqrt(2*np.sqrt(reaction**2+stopwatch_error**2))
t_dash_before=abs(T_10-T_20)/(np.sqrt(2*(reaction/5)**2+(stopwatch_error/5)**2))
t_dash=abs(T_10_again-T_20_again)/(np.sqrt(2*(reaction/5)**2+(stopwatch_error/5)**2))
l=26.25/100
l_of_bend=1/100
l_of_mass=(7.2/2)/100
l_of_hook=3/100
accurate_l=l-l_of_bend+l_of_hook+l_of_mass
def g(x,y):
    g=4*(np.pi**2)*(y)/((x)**2)
    return g
print("g_10 before optimation is:",g(T_10,l))
print("g_20 before optimation is:",g(T_20,l))
print("t' before optimization is:",t_dash_before)
print("g_10 after optimation is:",g(T_10_again,accurate_l))
print("g_20 after optimation is:",g(T_20_again,accurate_l))
print("t' after optimization is:",t_dash)
