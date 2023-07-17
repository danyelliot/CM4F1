#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 13:07:26 2021

@author: angel
"""
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline


def g(x):
    #gx = np.cos(3*x)   # T = 2*np.pi/3
    gx = np.cos(x/3) + np.cos(x/4)  # T = 24*np.pi
    #gx = 6*(np.sin(2*x))**2 + 5   # T = np.pi/2
    gx = np.log(2 + np.cos(x/2))  # T = 4 *np.pi
    #gx = np.sin(x/2)+3
    #gx = 2*x - x**2/np.pi
    #gx = 2*np.cos(x/2) + 3
    return gx

def f(x,T):
    fx = g(x*T/(2*np.pi))
    #fx = 2*x - x**2/np.pi
    return fx


n = 3
T = 24*np.pi #2*np.pi #4*np.pi #np.pi/2 #24*np.pi #2*np.pi/3

P = np.zeros(((2*n+1),2))
#thetak = np.array(((2*n+1),1))
for k in range(0,2*n+1):
    print(k)
    P[k,0] = 2*k*np.pi/(2*n+1)
    P[k,1] = f(P[k,0],T) 


print(P)

C_real = np.zeros(((2*n+1),2))
a = np.zeros(((2*n+1),1))
b = np.zeros(((2*n+1),1))
C = C_real.view(dtype=np.complex128)
#print(C)

for j in range(-n,n+1):
    #C[j+n] = 0
    for k in range(0,2*n+1):
        #print('k = ',k)
        C[j+n] = C[j+n] + np.exp(-j*complex(0,1)*complex(P[k,0],0))*complex(P[k,1],0)
    C[j+n] = C[j+n]/(2*n+1)
    print('Término j = {0:d} es C({1:d}) = ({2.real:.5f} + {2.imag:.5f}i)'.format(j+n,j,complex(C[j+n])))
    
    #print('C(j) = {0:.6f}'.format(float(C[j+n-1])))

for j in range(1,n+1):
    a[j] = 2*C[j+n].real
    b[j] = -2*C[j+n].imag 
    print('Parte real a({0:d}) = {1:.5f}'.format(j,float(2*C[j+n].real)))
    print('Parte imaginaria b({0:d}) = {1:.5f}'.format(j,float(2*C[j+n].imag)))
    # print('C:{:.2f}'.format(complex(C[j])))
    #print('C({0:.6f}) = {1:.6f}'.format(j,C[j]))

#actualizando a[0]
a[0] = C[n].real

Ptheta = a[0]
theta = np.linspace(0,2*np.pi,num=50)

for j in range(1,n+1):
    Ptheta = Ptheta + a[j]*np.cos(j*theta) + b[j]*np.sin(j*theta)
    
plt.plot(theta,Ptheta)
plt.plot(P[:,0],P[:,1],'o')
#plt.plot(theta,f(theta,T),'g')
plt.show()
    

