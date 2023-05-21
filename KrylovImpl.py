import numpy as np
import scipy.linalg as sl
import sympy as sp
import sys

def krylov(A,e):
  nrowA=np.shape(A)[0]
  B=np.zeros_like(A)
  colB=e
  B[:,nrowA-1]=colB.T
  print("row={}:\n B={}".format(nrowA-1,B))
  for k in range(nrowA-2,-1,-1):
    colB=np.dot(A,colB)
    print("colB={}".format(colB))
    B[:,k]=colB.T
    print("row={}:\n B={}".format(k,B))
  c=-1*np.dot(A,colB)
  if np.isclose(sl.det(B),0.0):
    sys.exit("Matrix B singular elegir otro e")
  a=sl.solve(B,c)
  x=sp.symbols("x")
  return sp.Lambda(x,x**nrowA+sum(a[k]*x**(nrowA-k-1) for k in range(nrowA)))

A = np.array([[0.5, 0.3, 0.5],
                [0.25, 0.4, 0.25],
                [0.25, 0.3, 0.25]],float)

y0 = np.array([1.0, 0.0, 0.0])
print("Alumno: Calle Cuadros Sergei")
print("Pregunta 3.B")
m=krylov(A,y0)
print(m)
