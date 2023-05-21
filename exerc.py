import math
import numpy as np
from numpy.core.fromnumeric import transpose

def gradienteConjugado(A,B,tol):
    x=np.zeros_like(B)
    r=B
    d=(np.linalg.norm(r))**2
    k=1
    while math.sqrt(d)>tol*np.linalg.norm(B) and k<=100:
        if k == 1: 
            p=r
        else:
            b=d/auxD2
            p=r+b*p
        w=np.dot(A,p)
        a=d/(np.dot(np.transpose(p),w))
        x=x+a*p
        r=r-a*w
        auxD2=d
        d=(np.linalg.norm(r))**2
        print("La matriz X",(k)," es:")
        print(x)
        #print (x[:,1])
        k+=1

def matriz(n):
    A=np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if j==i:
                A[i,j]=4
            elif (j==i+1 and i%3!=2) or (j==i-1 and j%3!=2) or j==i+3 or j==i-3  :
                A[i,j]=-1
    return A


def matriz2(n):
    A=np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if j==i:
                A[i,j]=4
            elif (j==i+1 and i%4!=3) or (j==i-1 and j%4!=3) or j==i+4 or j==i-4  :
                A[i,j]=-1
    return A

""" A=matriz(6)
b=np.transpose(np.array([0,5,0,6,-2,6]))
tol=1E-6
gradienteConjugado(A,b,tol) """

tol=1E-5
b = np.array([1.902207, 1.051143, 1.175689, 3.480083, 0.819600, -0.264419, -0.412789, 1.175689, 0.913337
, -0.150209, -0.264419, 1.051143, 1.966694, 0.913337, 0.819600, 1.902207])
b=np.transpose(b)
A=matriz2(16)
gradienteConjugado(A,b,tol)
