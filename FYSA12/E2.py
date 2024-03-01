# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:08:19 2024

@author: Aira
"""

import numpy as np 
import matplotlib.pyplot as plt 
import numpy.linalg as la
from matplotlib.patches import *

L_1=24.93/100
l=6.425/100
L_s=(30.000/100)*2
N=L_s/.01*10
D=22.83/100
m=.05/1000
g=9.81
I1=[0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2]
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
delta_x=.5/100
x0=117/1000
I_s_0=2.5
I_s=[.8,1.6,2.4,3.2]
U_H=[0.27/1000,0.53/1000,0.79/1000,1.27/1000]
mu_0=4*np.pi*10**(-7)
c=.05 #x/I
B_theo=(mu_0*(I_s_0)*N)/(np.sqrt(L_s**2+D**2))
B_theoretical=(mu_0*(np.array(I_s))*N)/(np.sqrt(L_s**2+D**2))
B_exp=m*g*c/l/L_1
print(B_exp)
print(B_theo)
print(B_theoretical)
plt.scatter(I1,list(np.array(x)*delta_x), marker="+", color="red", label="c=x/I_c")
plt.plot(I1,list(np.array(x)*delta_x))
plt.legend()
plt.xlabel("I_c")
plt.ylabel("x")
plt.rcParams['figure.dpi']=1000
I_c=.004
U_h=.79/1000
K_H=((np.array(U_H))/B_theoretical/I_c)
plt.plot(list(B_theoretical),list(np.array(U_H)/I_c))
print((np.array(U_H))/B_theoretical/I_c)
K_H_avg=sum(K_H)/len(K_H)
U_H_S=.09/1000
U_H_N=.06/1000
U_H_2=(U_H_S-U_H_N)/2
B_E=U_H_2/K_H_avg/I_c
print(B_E)
