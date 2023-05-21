import math
import numpy as np
from numpy.core.fromnumeric import transpose

def gradienteConjugado(A,B,tol):
    x=np.transpose([-5.05, 80.05, 0])
    r=B
    d=(np.linalg.norm(r))**2
    k=1
    while math.sqrt(d)>tol*np.linalg.norm(B):
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
        print (x[:,1])
        k+=1

def matrizHilbert(n):
  A=np.zeros((n, n))
  B=np.zeros((n,1))
  for i in range(0,n):
    aux=0
    for j in range(0,n):
      A[i,j]=1/(3+i+j)
      aux+=A[i,j]
    B[i,0]=(1/3)*aux
  return A,B

#tol = np.finfo(float).eps
tol =1.0e-5
for i in range(2,10):
  print("Para la matriz de hilbert de orden "+str(i)+" el desarrollo es: ")
  A,B=matrizHilbert(i)
  gradienteConjugado(A,B,tol) 

