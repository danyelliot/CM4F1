from math import log

def newton(f1,f2, a, b, tol=1.0e-12):
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    x0=0
    x = (a + b) / 2.0
    i=0
    while abs(x-x0) >= tol and i<100:
        x0 = x
        x = x0-f1(x0)/f2(x0)
        i+=1
    print("El número de iteraciones es: ",i)
    return x

def PuntoFijo(f, x0, tol=1.0e-6):
    max_iter=100
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    i=0
    while abs(f(x0)-x0) >= tol and i<max_iter:
        x0 = f(x0)
        i+=1
    if abs(f(x0)-x0) >= tol:
        print('El metodo no converge')
    else:
        print("Solucion aproximada por Punto Fijo: ",x0)
        print("El numero de iteraciones es: ",i)

def PuntoFijo(f, x0, tol=1.0e-4):
    max_iter=100
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    i=0
    while abs(f(x0)-x0) >= tol and abs(f(x0)-x0)<1E8 and i<max_iter:
        x0 = f(x0)
        i+=1
    if abs(f(x0)-x0) >= tol or i>max_iter:
        print('El metodo no converge')
    else:
        print("Solucion aproximada por Punto Fijo: ",x0)
        print("El numero de iteraciones es: ",i)

def secante(f, a, b, tol=1.0e-6):
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    #x0=0
    x0=0.4
    x = (a + b) / 2.0
    i=0
    while abs(x-x0) >= tol:
        aux=x0
        x0 = x
        x = x0-f(x0)*(x0-aux)/(f(x0)-f(aux))
        i+=1
    print("El número de iteraciones es: ",i)
    return x

def funcion1(x):
    return x+log(x)

def derivada1(x):
    return 1+1/x

def funcion2(x):
    return x**2-10

def derivada2(x):
    return 2*x

print('\nPregunta 1:\n')

print('Metodo de punto fijo')
PuntoFijo(funcion2,4,1.0e-4)

print('\nMetodo de la secante')
x=secante(funcion2, 3,4,1.0e-4)
print("La solucion es: ",x)

print('\nMetodo de Newton')
x=newton(funcion2,derivada2, 3,4, tol=1.0e-4)
print("La solucion son: ",x)

print('\nPregunta 4:\n')

print('Metodo de punto fijo')
PuntoFijo(funcion1,2,1.0e-4)

print('\nMetodo de la secante')
x=secante(funcion1, 0.5,1,1.0e-4)
print("La solucion es: ",x)

print('\nMetodo de Newton')
x=newton(funcion1,derivada1, 0.5,1, tol=1.0e-4)
print("La solucion son: ",x)
