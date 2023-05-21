import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
np.set_printoptions(precision = 9,suppress=True)


def diferenciasDividas(xi,fi):    
    titulo = ['i   ','xi  ','fi  ']
    n = len(xi)
    ki = np.arange(n)
    tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
    tabla = np.transpose(tabla)
    dfinita = np.zeros(shape=(n,n-1),dtype=float) #Si falla cambiar n-1 por n
    tabla = np.concatenate((tabla,dfinita), axis=1)
    [n,m] = np.shape(tabla)
    diagonal = n-1
    j = 3
    
    while (j < m):
        titulo.append('F['+str(j-2)+']')
        i = 0
        paso = j-2
        while (i < diagonal):
            denominador = (xi[i+paso]-xi[i])
            numerador = tabla[i+1,j-1]-tabla[i,j-1]
            tabla[i,j] = numerador/denominador
            i = i+1
        diagonal = diagonal - 1
        j = j+1
    
    dDividida = tabla[0,3:]
    n = len(dfinita)
    x = sym.Symbol('x')
    polinomio = fi[0]
    
    for j in range(1,n):
        factor = dDividida[j-1]
        termino = 1
        for k in range(0,j,1):
            termino = termino*(x-xi[k])
        polinomio = polinomio + termino*factor
    
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
    plt.title('Diferencias Divididas - Newton')
    plt.show()


xi = np.array([1,1.3,1.6,1.9,2.2])
fi = np.array([0.7651977,0.6200860,0.4554022,0.2818186,0.1103623])

diferenciasDividas(xi,fi)