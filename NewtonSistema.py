import numpy as np

def MetodoNewton(J,f,x,tol=1.0e-6):
  k=0
  x=x
  while np.linalg.norm(f(x)) > tol:
    x=x-np.transpose(np.linalg.solve(J(x),f(x)))
    k+=1
    x=x.ravel().tolist()
    print("La solucion para la iteracion numero",k,"es: ")
    print(x)
  print("El metodo termino con "+str(k)+" iteraciones")
  print('La respuesta es: ')
  print(np.round(x,6))

def J(x):
  Jf=np.zeros((2,2))
  Jf[:,0]=np.transpose([2*x[0],3])
  Jf[:,1]=np.transpose([2*x[1],-1])
  return Jf

def f(x):
  ft=np.zeros((2, 1))
  ft[0,0]=x[0]**2+x[1]**2-13
  ft[1,0]=3*x[0]-x[1]-3
  return ft

x0=[1.,1.]
MetodoNewton(J,f,x0)