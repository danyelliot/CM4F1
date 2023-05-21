import numpy as np
from math import sin
def ReglaFalsa(f, a, b, tol=1.0e-6):
    if a > b:
      raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0:
      raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
      raise ValueError("La cota de error debe ser un número positivo")
    i=1
    x=a-f(a)*(a-b)/(f(a)-f(b))
    while abs(f(x)) > tol and abs(x-b) > tol and i<100:
      if f(x)==0:
        a=b=x
      elif np.sign(f(x))*np.sign(f(a))<0:
        b=x
      else: 
        a=x
      x = a-f(a)*(a-b)/(f(a)-f(b))
      print('Intervalo para la iteracion ',i,' es: [',a,',',b,']')
      i+=1
    print("Solucion aproximada por Regla falsa: ",x)
    print("El numero de iteraciones es: ",i-1)


def ReglaFalsaModificada(f, a, b, tol=1.0e-6):
    if a > b:
      raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0:
      raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
      raise ValueError("La cota de error debe ser un número positivo")
    k=1
    x = b-f(b)*(b-a)/(f(b)-f(a))
    while abs(f(x)) > tol and abs(x-b) > tol and k<100:
      if np.sign(f(x))*np.sign(f(b))<0:
        a=b
        fa=f(a)
      else: 
        fa=0.5*f(a)
      b=x
      x = b-f(b)*(b-a)/(f(b)-fa)
      print('Intervalo para la iteracion ',k,' es: [',a,',',b,']')
      k=k+1
    print("Solucion aproximada por Regla falsa modificada: ",x)
    print("El numero de iteraciones es: ",k-1)

f= lambda x: x*sin(x)-1
print("Para el intervalo [1,2]:")
ReglaFalsa(f,1,2,1.0e-6)
ReglaFalsaModificada(f,1,2,1.0e-6)