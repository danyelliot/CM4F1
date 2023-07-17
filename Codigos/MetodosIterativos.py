import numpy as np

def verificar(A):
  m, n = A.shape
  if (m !=n ):
    print("La matriz no es cuadrada")
    return False
  return True

def matrizE(A):
	n=len(A)
	E=np.zeros_like(A)
	E=np.zeros_like(A)
	for i in range(n):
		for j in range(n):
			if i>j:
				E[i][j]=-A[i][j]
	return E

def iterativo(M,c,tol=1E-3):
  x=[0,0,0,0]
  aux=x
  print("El x en la iteracion 0  es: ",x)
  x=np.dot(M,x)+c
  i=1
  while np.linalg.norm(x-aux, np.inf)/ np.linalg.norm(x, np.inf)>tol:
    print("El x en la iteracion",i," es: ",x)
    aux=x
    x=np.dot(M,x)+c
    i=i+1
  print("El numero de iteraciones es: ", i)
  print("La respuesta en la iteración ",i," es:",x)


def GaussSeidel(A,b):
  D=np.diag(np.diag(A))
  E= matrizE(A)
  aux=D-E
  F=aux-A
  inv=np.linalg.inv(aux)
  G=np.dot(inv,F)
  print("LA MATRIZ DE GAUSS-SEIDEL ES: ")
  print(G)
  autovalores,autovectores=np.linalg.eig(G)
  print('Los autovalores son: ')
  print(autovalores)
  c=np.dot(inv,b)
  iterativo(G,c)


def Richardson(A,b):
  n=len(A)
  I=np.identity(n)
  M=I-A
  print("LA MATRIZ DE JACOBI ES: ")
  print(M)
  autovalores,autovectores=np.linalg.eig(M)
  print('Los autovalores son: ')
  print(autovalores)
  iterativo(M,b)

def Jacobi(A,b):
  n=len(A)
  I=np.identity(n)
  D=np.diag(np.diag(A))
  invD=np.linalg.inv(D)
  J=I-np.dot(invD,A)
  print("LA MATRIZ DE JACOBI ES: ")
  print(J)
  autovalores,autovectores=np.linalg.eig(J)
  print('Los autovalores son: ')
  print(autovalores)
  c=np.dot(invD,b)
  iterativo(J,c)


A = np.array([[10,10,60,20],[10,100,20,40],[100,30,20,30],[5,10,5,30]],float)
b = np.array([140,190,105,54])
b=np.transpose(b)

Jacobi(A,b)
