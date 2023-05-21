from math import log,sin,cos,pi

def newton(f1,f2, a, b, tol=1.0e-12):
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    x0=0
    x = (a + b) / 2.0
    i=0
    while abs(x-x0) >= tol and i<100:
        print('Para la iteracion ',i)
        print('x=',x,'  f(x)=',f1(x),'f\'(x)=',f2(x))
        x0 = x
        x = x0-f1(x0)/f2(x0)
        i+=1
    print('Para la iteracion ',i)
    print('x=',x,'  f(x)=',f1(x))
    print("El número de iteraciones es: ",i)
    return x


def newtonModificado1(f1,f2, a, b, tol=1.0e-12): #segun el libro de tecnicas...
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    x0=0
    x = (a + b) / 2.0
    fx0=f2(x)
    i=0
    while abs(x-x0) >= tol and i<100:
        print('Para la iteracion ',i)
        print('x=',x,'  f(x)=',f1(x),'f\'(x)=',f2(x))
        x0 = x
        x = x0-f1(x0)/fx0
        i+=1
    print('Para la iteracion ',i)
    print('x=',x,'  f(x)=',f1(x))
    print("El número de iteraciones es: ",i)
    return x

def newtonModificado2(f1,f2,f3, a, b, tol=1.0e-12): #este si es una mejora
    if tol <= 0:
        raise ValueError("La cota de error debe ser un número positivo")
    x0=0
    x = (a + b) / 2.0
    i=0
    while abs(x-x0) >= tol and i<100:
        print('Para la iteracion ',i)
        print('x=',x,'  f(x)=',f1(x),'f\'(x)=',f2(x))
        x0 = x
        x = x0-(f1(x0)*f2(x0))/(f2(x0)**2-f1(x0)*f3(x0))
        i+=1
    print('Para la iteracion ',i)
    print('x=',x,'  f(x)=',f1(x))
    print("El número de iteraciones es: ",i)
    return x

funcion=lambda x: x-0.8-0.2*sin(x)
derivada=lambda x: 1-0.2*cos(x)
segundaDerivada=lambda x: 0.2*sin(x)
x=newton(funcion,derivada, 0,2, tol=1.0e-6)
print("La solucion es: ",x)
x=newtonModificado1(funcion,derivada, 0,pi/2, tol=1.0e-6)
print("La solucion es: ",x)
x=newtonModificado2(funcion,derivada,segundaDerivada, 0,pi/2, tol=1.0e-6)
print("La solucion es: ",x)