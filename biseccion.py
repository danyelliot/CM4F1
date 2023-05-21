from math import sin, sqrt,log

def biseccion(f, a, b, tol=1.0e-6):
    if a > b:
      raise ValueError("Intervalo mal definido")
    if f(a) * f(b) >= 0:
      raise ValueError("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
      raise ValueError("La cota de error debe ser un número positivo")
    i=c=0
    while abs(a-b)>=tol:
      i+=1
      c=(a+b)/2
      if f(c)==0:
        a=b=0
      elif f(b)*f(c)>=0:
        b=c
      else:
        a=c
      print('Intervalo para la iteracion ',i,' es: [',a,',',b,']')
    print('El numero de iteraciones es: ',i)
    return c

f= lambda x: x*sin(x)-1
# Metodo de Biseccion
sol = biseccion(f,1,2,1.0e-3)
print("Solucion aproximada por Biseccion: ",sol)