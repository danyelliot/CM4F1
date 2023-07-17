import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
np.set_printoptions(precision = 9,suppress=True)

def HermiteInterpolacion(xi,fi,f1i):    
    
    titulo = ['i   ','xi  ','fi  ']
    n = len(xi)*2
    ki = np.arange(n)
    xj=[]
    fj=[]
    for xk in xi:
        xj.append(xk)
        xj.append(xk)
    for fk in fi:
        fj.append(fk)
        fj.append(fk)
    
    tabla = np.concatenate(([ki],[xj],[fj]),axis=0)
    tabla = np.transpose(tabla)
    dfinita = np.zeros(shape=(n,n-1),dtype=float)
    tabla = np.concatenate((tabla,dfinita), axis=1)
    [n,m] = np.shape(tabla)
    diagonal = n-1
    j = 3
    
    while (j < m):
        titulo.append('F['+str(j-2)+']')
        i = 0
        paso = j-2
        while (i < diagonal):
            if j==3 and i%2==0:
                idx=int(i/2)
                tabla[i,j]=f1i[idx]
                i+=1
                continue
            denominador = (xj[i+paso]-xj[i])
            numerador = tabla[i+1,j-1]-tabla[i,j-1]
            tabla[i,j] = numerador/denominador
            i = i+1
        diagonal = diagonal - 1
        j = j+1
    print(tabla)
    dDividida = tabla[0,3:]
    n = len(dfinita)
    x = sym.Symbol('x')
    polinomio = fi[0]
    
    for j in range(1,n):
        factor = dDividida[j-1]
        termino = 1
        for k in range(0,j,1):
            termino = termino*(x-xj[k])
        aux=termino*factor
        polinomio = polinomio + aux
    polisimple = polinomio.expand()
    px = sym.lambdify(x,polisimple)
    muestras = 101
    a = np.min(xi)-3
    b = np.max(xi)+3
    pxi = np.linspace(a,b,muestras)
    pfi = px(pxi)
    print('Tabla Diferencia Dividida')
    print([titulo])
    print(tabla)
    print('dDividida: ')
    print(dDividida)
    print('polinomio: ')
    print(polinomio)
    print('polinomio simplificado: ' )
    print(polisimple)
    plt.plot(xi,fi,'o', label = 'Puntos')
    plt.plot(pxi,pfi, label = 'Polinomio')
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Polinomio de hermite')
    plt.show()


xi = np.array([1.3,1.6,1.9])
fi = np.array([0.6200860,0.4554022,0.2818186])
f1i= np.array([-0.5220232,-0.5698959,-0.5811571])

HermiteInterpolacion(xi,fi,f1i)