from math import log,sin
import numpy as np
def secante(f, a, b, tol=1.0e-6):
  if a > b:
    raise ValueError("Intervalo mal definido")
  if f(a) * f(b) >= 0:
    raise ValueError("La función debe cambiar de signo en el intervalo")
  if tol <= 0:
    raise ValueError("La cota de error debe ser un número positivo")
  x0=a
  x=b
  i=0
  while abs(f(x)) > tol and i<100:
      aux=x0
      x0=x
      x = x0-f(x0)*(x0-aux)/(f(x0)-f(aux))
      i+=1
      print('Para la iteracion ',i)
      print('x_',i+1,'=',x,'f(x_',i+1,')','=',f(x))
  print("El número de iteraciones es: ",i)
  return x

f= lambda x: np.cos(x) - x*(np.e)**x 
print("La solucion es: ",secante(f,0,1,1.0e-5))

