import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def Matrixmonde(n,puntos):
    A=np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[j,i]=(puntos[j][0]**i)
    return A


def CoeficientesIndeterminados(A,n,puntos):
    lista=list()
    for j in range(n):
        lista.append(puntos[j][1])
    b=np.transpose(np.array(lista))
    c=np.dot(np.linalg.inv(A),b)
    return c


puntos=np.array([[-1,1],[2,-1],[0,-1]])
n=len(puntos)
A=Matrixmonde(n,puntos)
inv=np.linalg.inv(A)
coeficientes=CoeficientesIndeterminados(A,n,puntos)
print(coeficientes)
x=sp.symbols("x")
m=sp.Lambda(x,sum(coeficientes[k]*x**(k) for k in range(n)))
print(m)
muestras = 101
xi=puntos[:,0]
fi=puntos[:,1]
a = np.min(xi)-3
b = np.max(xi)+3
pxi = np.linspace(a,b,muestras)
pfi=[]
for i in range(muestras):
    pfi.append(m(pxi[i]))
plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Coeficientes indeterminados')
plt.show()

