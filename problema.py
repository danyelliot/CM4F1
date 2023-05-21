import numpy as np
def metodoIterativo(A,M,b,x):
  aux=0
  bandera=True
  k=1
  while bandera and k<100:
    aux=x
    x=-np.dot(np.dot(np.linalg.inv(M),A-M),x)+np.dot(np.linalg.inv(M),b)
    if(np.linalg.norm(x-aux, np.inf)<=1E-4):
      bandera=False
    k+=1
    if(k==100):
      print("El metodo diverge")
      return
  print("Calle Cuadros sergei-20184099J")
  print("Pregunta 4")
  print("El numero de iteraciones es: "+str(k-1))
  return x

A= np.array([[8,2,-3],[-3,9,4],[3,-1,7]],float)
M= np.array([[8,2,0],[-3,9,0],[0,0,7]],float)
b=np.transpose(np.array([-20,62,0],float))
x=np.transpose(np.array([0,0,0],float))
x= metodoIterativo(A,M,b,x)
print("La solucion es:")
print(x)

