import math
import numpy as np
import sympy as sp
from sympy import cos,sin
import matplotlib.pyplot as plt
from scipy.fftpack import fft
a=list()
b=list()
dt=30
x=range(0,331,dt)
y=np.array([408,89, -66 ,10, 338, 807, 1238, 1511, 1583, 1462, 1183, 804])
n= len(x)
w=2*np.pi/(n*dt)
d=fft(y)/n
print(d)
def f(x,n=n,d=d):
    M=math.floor((n+1)/2)
    a=2*d.real
    b=-2*d.imag
    a[0]/=2
    a[M]/=2
    y=0
    for k in range(0,M+1):
        y+= a[k] * np.cos(w * k * x) + b[k] * np.sin(w * k * x)
    wx=sp.symbols('wx')
    m=sp.Lambda(wx,sum(a[k] * cos(k * wx) + b[k] * sin(k * wx) for k in range(0,M+1)))
    print(m)
    return y

tx= np.linspace(0,360,1000)
ty=f(tx)
plt.plot(tx,ty,'o',label = 'Transformada')
plt.plot(x,y,'o',color='red',label = u"Puntos")
plt.legend()
plt.xlabel('Ascensión (grados)')
plt.ylabel('Declinación (minutos)')
plt.title('Posición del asteroide Pallas')
plt.show()