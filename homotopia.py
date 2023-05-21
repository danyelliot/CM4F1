import numpy as np
from math import e, log,cos, pi,sin
def J(x):
    Jf=np.zeros((3,3))
    Jf[:,0]=np.transpose([3,2*x[0],-x[1]*e**(-x[0]*x[1])])
    Jf[:,1]=np.transpose([x[2]*sin(x[1]*x[2]),-162*(x[1] + 0.1),-x[0]*e**(-x[0]*x[1])])
    Jf[:,2]=np.transpose([x[1]*sin(x[1]*x[2]),cos(x[2]),20])
    return Jf

def f(x):
    ft=np.zeros((3, 1))
    ft[0,0]=3*x[0]- cos(x[1]*x[2])-0.5
    ft[1,0]=x[0]**2-81*(x[1] + 0.1)**2 + sin(x[2]) + 1.06
    ft[2,0]=e**(-x[0]*x[1]) + 20*x[2] +(10*pi- 3)/3
    return ft

def homotopia():
    pass

def G(a,x0):
    pass