import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from functools import reduce

def lagrange(puntos):
    n=len(puntos)
    funcion=0
    for i in range(n):
        xi=puntos[i,0]
        yi=puntos[i,1]
        aux=1
        diferentes=[]
        for j in range(n):
            if i!=j:
                xj=puntos[j,0]
                diferentes.append(xj)
                aux*=1/(xi-xj)
        x=sp.symbols("x")
        mi=sp.Lambda(x,aux*reduce(lambda x, y: x*y, (x-xj for xj in diferentes)))
        print('La funcion L',str(i),' es: ',mi)
        funcion+=yi*mi.expr
    x=sp.symbols("x")
    funcion=sp.Lambda(x,funcion)    
    print('El polinomio de interpolación es: ',funcion)
    funcred=funcion.expand()
    print('El polinomio de interpolación reducido es: ',funcred)
    return funcred


puntos=np.array([[-1,2],[0,1],[-2,3],[1,0]])
func=lagrange(puntos)
muestras = 101
xi=puntos[:,0]
fi=puntos[:,1]
a = np.min(xi)-3
b = np.max(xi)+3
pxi = np.linspace(a,b,muestras)
pfi=[]
for i in range(muestras):
    pfi.append(func(pxi[i]))
plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Metodo Lagrange')
plt.show()