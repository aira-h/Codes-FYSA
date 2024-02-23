# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:18:59 2024
@author: Aira
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy.linalg as la
from matplotlib.patches import *
d=50/1000
r=9.55/1000
m_2=1.5
m_1=38.3/1000
b=3/100
c=5.3/100
L=188.1/100
a=(b+c)/2
j_1_initial=0
I=2*m_1*(d**2+(2/5*(r**2)))
"""The above values are all provided in the manual"""
error_bc=.05/100
error_a=np.sqrt((error_bc**2)/2+(error_bc**2)/2)
error_j=.05/100
error_y=np.sqrt((error_j**2)/2+(error_j**2)/2)
error_d=.0002
error_m_2=0.01
error_L=0.0005
error_T=10
"""These values are the errors"""
j_2=[1.5,2.3,2.9,3.5,4.4,5.1,6,6.8,7.4,7.9,8.4,8.8,8.9,8.9,8.8,8.5,8.1,7.5,6.9,
     6.2,5.5,4.7,4,3.2,2.6,2,1.5,1.1,0.9,0.7,0.8,0.8,1.1,1.5,2,2.5,3.3,3.9,4.6,
     5.4,6,6.6,7.2,7.6,8,8.2,8.3,8.3,8.1,7.8,7.5,7.1,6.4,5.9,5.2,4.5,3.9,3.3,
     2.7,2.2,1.8,1.5,1.2,1.2,1.2,1.4,1.6,2.1,2.5,3,3.7,4.3,4.9,5.5,6.1,6.5,7.1,
     7.4,7.6,7.8,7.9,7.8,7.7,7.4,7.1,6.7,6.1,5.5,5,4.5,3.9,3.4,2.9,2.4,2,1.9,
     1.6,1.6,1.7,1.9,2.1,2.5,3,3.5,4,4.5,5,5.5,6,6.5,6.9,7.1,7.3,7.5,7.5,7.4,
     7.2,7,6.6,6.3,5.8,5.3,4.8,4.3,3.8,3.3,2.9,2.6,2.3,2.1,2,2,2.1,2.3,2.5,2.8,
     3.3,3.7,4.2,4.7,5.2,5.5,6,6.4,6.7,7,7.1,7.1,7.2,7,6.8,6.6,6.2,5.9,5.5,5,
     4.6,4.2,3.7,3.4,3,2.7,2.5,2.4,2.4,2.4,2.5,2.6,2.9,3.2,3.6,4,4.4,4.8,5.3,
     5.6,6,6.4,6.5,6.6]
j_1=[2.7,2.1,1.5,0.9,0.2,-0.5,-1.3,-1.8,-2.4,-3.4,-3.5,-3.9,-4.1,-4.4,-4.2,-4.1,
     -3.8,-3.5,-3,-2.5,-1.9,-1.3,-0.6,0,0.7,1.3,1.8,2.3,2.6,2.8,2.9,2.9,2.6,2.4
     ,2.1,1.6,1.1,0.5,-0.6,-1.4,-1.9,-2.4,-2.9,-3.3,-3.5,-3.8,-3.8,-3.8,-3.4,-3
     ,-2.6,-2.1,-1.5,-1,-0.4,0.1,0.7,1.2,1.6,2,2.3,2.4,2.5,2.5,2.2,2.1]
time_1=list(np.linspace(0, 1020, len(j_1)))
time_2=list(np.linspace(15, 2700, len(j_2)))
peaks=[]
troughs=[]
for i in range(len(j_1)):
    if i>0 and i<(len(j_1)-1):
        if j_1[i]>=j_1[i-2] and j_1[i]>=j_1[i-1] and j_1[i]>=j_1[i+1] and j_1[i]>=j_1[i+2]:                    
            peaks.append(j_1[i])
        if j_1[i]<=j_1[i-2] and j_1[i]<=j_1[i-1] and j_1[i]<=j_1[i+1] and j_1[i]<=j_1[i+2]:
            troughs.append(j_1[i])
peaks=list(set(peaks))
troughs=list(set(troughs))
for i in peaks[:]:
    if i in troughs:
        peaks.remove(i)
for i in troughs[:]:
    if i in peaks:
        troughs.remove(i) 
peaks.sort(reverse = True)
troughs.sort()
"""To calculate the turning points, also note that the code was modified at one point to find the turning points for
 J_2 and then to find the Time period for that, see below"""
j_1_eq=(peaks[0]+3*troughs[0]+3*peaks[1]+troughs[1])/8
def oscillating_function(t, A, omega, phi, C):                                 
    return A * np.sin(omega * t + phi) + C     
"""As it is an oscillating function"""                                
initial_guess = (1, 1, 0, 0)
plt.plot(time_2,j_2 , label='J_2')
plt.plot(time_1,j_1 , label='J_1')
plt.plot([0,1000],[j_1_eq/2,j_1_eq/2],label='J_1_eq', color="red")
"""plotting"""
params, params_covariance = curve_fit(oscillating_function, np.array(time_1), np.array(j_1), p0=initial_guess)
plt.plot(time_1, oscillating_function(np.array(time_1), *params), color='green', label='Curve fit for J_1')
print("Fitted parameters for j_1: (A, omega, phi, C):", params)
j_1_final=j_1_eq/2
j_1_f=params[3]
"""Kept just to show that the turning point method is inaccurate later, also to note there is no divide by 2 as the oscillation curve fit will give the exact J_1"""
params, params_covariance = curve_fit(oscillating_function, np.array(time_2), np.array(j_2), p0=initial_guess)
plt.plot(time_2, oscillating_function(np.array(time_2), *params), color='purple', label='Curve fit for j_2')
print("Fitted parameters for j_2: (A, omega, phi, C):", params)
print()
j_2_final=params[3]
plt.grid(which = "both")
plt.minorticks_on()
plt.tick_params(which = "minor", bottom = False, left = False)
plt.legend()
plt.xlabel('Time')
plt.ylabel("j")
plt.title('j vs t')
plt.rcParams['figure.dpi'] = 10
T=(450-202.5 + 975-712.5 + 1477.5-1230 + 1987.5-1732.5 + 2490-2250 + 502.5-240 + 952.5-705)/7*2
"""The period is always peak to peak, but to get a more accurate reading its taken as one peak to the other peak times 2 and then the average of all the values, note that the last two values are from j_1 and the others from j_2"""
def G(x):
    y=(abs(x-j_2_final)/2)/100
    s=d*y/(2*L)
    R=a-s
    theta=.5*np.arctan(y/L)
    G_1=(4*(np.pi**2)*I*(R**2)*theta)/(2*d*(T**2)*m_1*m_2)
    beta=(a*(a-s)**2)/(((a**2)+4*(d**2))**(3/2))
    G_2=((4*(np.pi**2)*((a-s)**2)*theta)/(d*(1-beta)*(T**2)*m_2))*(d**2+(2/5*(r**2)))
    sigma_t=np.sqrt((2*error_a/a)**2 + (error_y/y)**2 + (error_d/d)**2 + (error_m_2/m_2)**2 + (error_L/L)**2 + (2*error_T/T)**2)
    if x==j_1_final:
        print("Using the turning point equation for J_1, G_1 =",G_1,"Nm^2/kg^2")
        print("And the error for that is:",sigma_t*G_1)
        print()
        print("Using the turning point equation for J_1, G_2 =",G_2,"Nm^2/kg^2")
        print("And the error for that is:",sigma_t*G_2)
    else:
        print("Using the curve fit equation for J_1, G_1 =",G_1,"Nm^2/kg^2")
        print("And the error for that is:",sigma_t*G_1)
        print()
        print("Using the curve fit equation for J_1, G_2 =",G_2,"Nm^2/kg^2")
        print("And the error for that is:",sigma_t*G_2)
"""The function to calculate G_1 and G_2 as well as the error and as I decided to calculate everything twice to show the turning point issue, the 
variables that are affected by j_1 are the only ones taken into the function, everything else is what the code initialized with"""
G(j_1_final)
print()
G(j_1_f)
