import numpy as np

def get_D(A):
  D=np.diag(np.diag(A))
  return D

def get_E(A):
  n=len(A)
  E=np.zeros((n, n))
  for i in range(n):
    for j in range(i):
      E[i][j]=-A[i][j]
  return E

def get_F(A):
  return get_D(A)-get_E(A)-A

def get_G(A,w):
  n=len(A)
  G=np.zeros((n, n))
  G= np.dot(np.linalg.inv(get_D(A)-w*get_E(A)),((1-w)*get_D(A) + w*get_F(A)))
  return G

def SOR(A,b,w,tol):
  n=len(A)
  aux=np.zeros((n, 1))
  x=np.transpose(np.array([1.,1.,1.],float))
  i=0
  while np.linalg.norm(x-aux, np.inf)/np.linalg.norm(x, np.inf)>tol :
    print('La solucion en la iteracion ',i,' es:',x)
    aux=x
    x=np.dot(get_G(A,w),x)+w*np.dot(np.linalg.inv(get_D(A)-w*get_E(A)),b)
    i+=1
    if i==100:
      return 'La solucion NO converge'
  print("La respuesta final es: ")
  return x


A = np.array([[3,-1,1],[-1,3,-1],[1,-1,3]],float)

b= np.transpose(np.array([-1,7,-7]))
#print(np.round(SOR(A,b,1.25,1E-6),4))
print(SOR(A,b,1.25,1E-6))

